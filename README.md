# Stockmarket Alerts & News
## Overview
Hello, I'm Mert, and today marks Day 36 of my "100 Days of Python" challenge. In this project, I've developed a Python script named main.py that provides Stock Market alerts and the latest news for a specified stock symbol. The example uses the TSLA (Tesla Inc) stock, but you can customize it for any stock of your choice.

## Project Description
The script fetches both stock market data and the latest news related to the specified stock symbol. It calculates the percentage change in stock prices and sends an SMS alert using the Twilio API. The SMS includes the stock symbol, percentage change, the headline, and a brief of the latest news.

How to Run
To use the StockMarket Alerts & News script, follow these steps:

* Open the Python script: `main.py`
   ```bash
   python main.py
   ```
* Fill in your Alpha Vantage API key, Twilio API credentials, and customize the stock symbol (default is TSLA).
* Ensure you have the required libraries installed (requests and twilio).
* Run the script to receive Stock Market alerts and news via SMS.
* Make sure you have Python installed on your system.
* Alternatively, you can set daily tasks and make them automatic by installing this programme at https://www.pythonanywhere.com/.

## Project Files
* main.py: The main Python script for fetching stock market data, news, and sending SMS alerts.
* README.md: This file, providing an overview and instructions for the project.
## Customization
You can customize the script for different stocks by modifying the STOCK variable in the main.py file. Additionally, feel free to adapt the script for your preferred functionalities.

## Dependencies
The project relies on the following Python libraries:

* requests: For making HTTP requests to fetch stock market data and news.
* twilio: For sending SMS alerts.
## Conclusion
I hope you find the StockMarket Alerts & News script helpful for staying informed about stock prices and relevant news. Feel free to explore, modify, and adapt the script to meet your specific needs. Happy coding!

Note: Remember to handle your API keys and sensitive information with care.
