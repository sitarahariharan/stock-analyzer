import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(stock_symbol):

    # fetch historical stock price data using Yahoo Finance API
    # stock_symbol - stock ticker symbol (ex. AAPL, TSLA)
    # return - dataframe with stock data

    try:
        # initialize connection to Yahoo Finance API
        stock = yf.Ticker(stock_symbol)
        
        # get 6 months of historical data
        df = stock.history(period="6mo")
        
        if df.empty:
            print(f"No data found for {stock_symbol}. Check the stock symbol.")
            return None
            
        # process date column for easier handling
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
        
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")
        return None

def calculate_sma(data, window):
    
    # calculate simple moving average (SMA)
    # data - dataframe with stock data
    # window - moving average window size
    # return - same dataframe with additional SMA column
    
    # calculate SMA using pandas rolling window function
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def plot_stock_data(data, stock_symbol, sma_window=None):
    
    # plot stock price + SMA trends
    # data - A DataFrame with stock data.
    # stock_symbol - stock ticker symbol
    # sma_window - SMA window size
    
    # create new figure with specified size
    plt.figure(figsize=(12, 6))
    
    # plot closing price
    plt.plot(data['Date'], data['Close'], label=f'{stock_symbol} Close Price', color='blue')
    
    # if SMA was calculated, add it to plot
    if sma_window:
        plt.plot(data['Date'], data[f'SMA_{sma_window}'], label=f'SMA_{sma_window}', color='orange')
    
    # add plot decorations
    plt.title(f"Stock Price and SMA for {stock_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # display welcome message + get user input
    print("Welcome to the Stock Price Analyzer!")
    stock_symbols = input("Enter stock symbols separated by commas (e.g., AAPL, TSLA): ").upper().split(',')
    
    # get SMA window size from user
    sma_window = None
    try:
        sma_window = int(input("Enter the SMA window size (e.g., 5, 10, 20): "))
    except ValueError:
        print("Invalid window size. Skipping SMA calculation.")
    
    # process each stock symbol entered by the user
    for stock_symbol in stock_symbols:
        stock_symbol = stock_symbol.strip()
        print(f"Fetching data for {stock_symbol}...")
        
        # fetch stock data
        stock_data = fetch_stock_data(stock_symbol)
        if stock_data is None or stock_data.empty:
            print(f"Failed to fetch or parse stock data for {stock_symbol}.")
            continue
            
        print(f"Data fetched successfully for {stock_symbol}!")
        
        # calculate SMA if window size was provided
        if sma_window:
            stock_data = calculate_sma(stock_data, sma_window)
            print(f"SMA_{sma_window} calculated for {stock_symbol}.")
        
        # save data to csv file
        filename = f"{stock_symbol}_stock_data.csv"
        stock_data.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
        
        # create + display plot
        plot_stock_data(stock_data, stock_symbol, sma_window)
    
    print("Thank you for using the Stock Price Analyzer!")

# entry point of program
if __name__ == "__main__":
    main()
