# Stock Price Analyzer

A Python application that fetches and analyzes historical stock price data using the Yahoo Finance API. The program allows users to visualize stock prices and calculate Simple Moving Averages (SMA) for multiple stocks.

## Features

- Fetch 6 months of historical stock data from Yahoo Finance
- Calculate Simple Moving Average (SMA) with customizable window size
- Generate interactive plots showing stock price trends and SMA
- Export stock data to CSV files for further analysis
- Support for analyzing multiple stocks in one session

### When prompted:
   - Enter one or more stock symbols (e.g., "AAPL, MSFT, GOOGL")
   - Specify the SMA window size (e.g., 20 for 20-day moving average)

### The program will:
   - Generate a plot for each stock
   - Save the data to CSV files named `{STOCK_SYMBOL}_stock_data.csv`, containing Date, Open + High + Low + Close prices, Volume, and SMA values if calculated
