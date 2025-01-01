import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(stock_symbol):
    """
    Fetch historical stock price data using Yahoo Finance API.
    :param stock_symbol: The stock ticker symbol (e.g., AAPL, TSLA).
    :return: A DataFrame with the stock data.
    """
    try:
        stock = yf.Ticker(stock_symbol)
        df = stock.history(period="6mo")  # Fetch data for the last 6 months
        if df.empty:
            print(f"No data found for {stock_symbol}. Check the stock symbol.")
            return None
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")
        return None

def calculate_sma(data, window):
    """
    Calculate Simple Moving Average (SMA).
    :param data: A DataFrame with stock data.
    :param window: The moving average window size.
    :return: The same DataFrame with an additional SMA column.
    """
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def plot_stock_data(data, stock_symbol, sma_window=None):
    """
    Plot stock price and SMA trends.
    :param data: A DataFrame with stock data.
    :param stock_symbol: The stock ticker symbol.
    :param sma_window: The SMA window size.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['Date'], data['Close'], label=f'{stock_symbol} Close Price', color='blue')
    if sma_window:
        plt.plot(data['Date'], data[f'SMA_{sma_window}'], label=f'SMA_{sma_window}', color='orange')
    plt.title(f"Stock Price and SMA for {stock_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    print("Welcome to the Stock Price Analyzer!")
    stock_symbols = input("Enter stock symbols separated by commas (e.g., AAPL, TSLA): ").upper().split(',')
    sma_window = None

    try:
        sma_window = int(input("Enter the SMA window size (e.g., 5, 10, 20): "))
    except ValueError:
        print("Invalid window size. Skipping SMA calculation.")

    for stock_symbol in stock_symbols:
        stock_symbol = stock_symbol.strip()
        print(f"Fetching data for {stock_symbol}...")
        stock_data = fetch_stock_data(stock_symbol)

        if stock_data is None or stock_data.empty:
            print(f"Failed to fetch or parse stock data for {stock_symbol}.")
            continue

        print(f"Data fetched successfully for {stock_symbol}!")
        if sma_window:
            stock_data = calculate_sma(stock_data, sma_window)
            print(f"SMA_{sma_window} calculated for {stock_symbol}.")

        # Save the data to a CSV file
        filename = f"{stock_symbol}_stock_data.csv"
        stock_data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")

        # Plot the data
        plot_stock_data(stock_data, stock_symbol, sma_window)

    print("Thank you for using the Stock Price Analyzer!")

if __name__ == "__main__":
    main()
