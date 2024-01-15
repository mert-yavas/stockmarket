import requests
from datetime import datetime, timedelta
from twilio.rest import Client

# ---------------------------- STOCK MARKET DATA ------------------------------- #
# Define the stock symbol and company name
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_MARKET_URL = "https://www.alphavantage.co/query"

# Set parameters for the Alpha Vantage API request
stock_market_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "YOUR_API_KEY"
}

# Make the API request to get stock market data
response = requests.get(STOCK_MARKET_URL, params=stock_market_parameters)
response.raise_for_status()
stock_data = response.json()

# Extract relevant stock market information
last_refreshed = stock_data["Meta Data"]["3. Last Refreshed"]
stripped_last_refreshed = datetime.strptime(last_refreshed, "%Y-%m-%d")
calculate_day_before = stripped_last_refreshed - timedelta(days=1)
day_before = calculate_day_before.strftime("%Y-%m-%d")

yesterday = float(stock_data["Time Series (Daily)"][last_refreshed]["4. close"])
day_before = float(stock_data["Time Series (Daily)"][day_before]["4. close"])

price_difference = yesterday - day_before
percentage = abs(round(price_difference / yesterday * 100, 2))

# Determine the price change direction
if price_difference > 0:
    difference = f"+%{percentage}"
else:
    difference = f"-%{percentage}"

# ---------------------------- NEWS DATA ------------------------------- #
# Set parameters for the News API request
NEWS_URL = "https://newsapi.org/v2/everything"
news_url_parameters = {
    "q": STOCK,
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": "YOUR_API_KEY"
}

# Make the API request to get news data
response_news = requests.get(NEWS_URL, params=news_url_parameters)
response_news.raise_for_status()
news_data = response_news.json()

# Extract the latest news headline and brief
title = news_data["articles"][0]["title"]
news = news_data["articles"][0]["description"]

# ---------------------------- SMS ------------------------------- #
# Twilio API configuration
ACCOUNT_SID = 'TWILIO ACCOUNT SID' 
AUTH_TOKEN = 'TWILIO TOKEN'
TWILIO_NUMBER = "YOUR TWILIO NUMBER"
RECEIVER_NUMBER = "YOUR GSM NUMBER"

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send SMS with stock market and news information
message = client.messages.create(
    from_=TWILIO_NUMBER,
    body=f"{STOCK}: {difference}\nHeadline: {title}\nBrief: {news}",
    to=RECEIVER_NUMBER
)
