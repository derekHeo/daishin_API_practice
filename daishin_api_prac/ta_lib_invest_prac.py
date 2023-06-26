import pandas as pd
import talib

# Load the stock data
stock_data = pd.read_csv("stock_data.csv")

# Calculate the SMA and RSI indicators
sma = talib.SMA(stock_data["Close"], timeperiod=20)
rsi = talib.RSI(stock_data["Close"], timeperiod=14)

# Initialize the variables
portfolio = 100000
shares = 0
cash = portfolio

# Backtest the strategy
for i in range(len(stock_data)):
    # Buy when SMA is above the close price and RSI is less than 30
    if sma[i] > stock_data["Close"][i] and rsi[i] < 30:
        shares += cash / stock_data["Close"][i]
        cash = 0
    # Sell when SMA is below the close price and RSI is more than 70
    elif sma[i] < stock_data["Close"][i] and rsi[i] > 70:
        cash += shares * stock_data["Close"][i]
        shares = 0

# Calculate the final portfolio value
portfolio = cash + shares * stock_data["Close"][-1]

# Print the final portfolio value
print("Final portfolio value:", portfolio)