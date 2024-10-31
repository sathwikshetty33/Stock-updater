This Python project checks the daily stock price fluctuations for a specific stock and sends the top news articles related to the company if the stock price changes significantly. The project uses the Alpha Vantage API for stock data, News API for news headlines, and Twilio's API for sending SMS alerts.

Table of Contents
Project Overview
Features
Technologies Used
Installation
Configuration
Usage
License
Project Overview
This project monitors the stock price of a specified company, Tesla Inc., identified by the stock symbol TSLA. If the price change (up or down) between yesterday and the day before yesterday exceeds a certain threshold, the script fetches the latest news headlines for the company and sends them to the user via SMS.

Features
Fetches daily stock prices for the chosen company.
Calculates the percentage change between the last two closing prices.
If the change is significant, retrieves the top 3 related news articles.
Sends SMS alerts with the stock price change and news headlines.
Technologies Used
Python 3.x
Alpha Vantage API - Stock price data
News API - News headlines
Twilio - SMS notifications
