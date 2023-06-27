import numpy as np
import talib
import matplotlib.pyplot as plt
import pandas as pd

# Load the stock data
stock_data = pd.read_csv("stock_data.csv")

# Calculate the SMA using the close prices
sma = talib.SMA(stock_data["Close"], timeperiod=20)

#스토케스틱
stochastic_oscillator = talib.STOCH(stock_data["High"], stock_data["Low"], stock_data["Close"],
                                     fastk_period=14, slowk_period=3, slowk_matype=0, 
                                     slowd_period=3, slowd_matype=0)

#RSI
rsi = talib.RSI(stock_data["Close"], timeperiod=14)

#볼린저 밴드
upper, middle, lower = talib.BBANDS(stock_data["Close"], timeperiod=20)

#MACD
macd, macd_signal, macd_hist = talib.MACD(stock_data["Close"],
                                           fastperiod=12, slowperiod=26, signalperiod=9)

#Aroon up / down
aroon_up, aroon_down = talib.AROON(stock_data["High"], stock_data["Low"], timeperiod=14)

# Plot the stock data and SMA
plt.figure(figsize=(15, 5))
plt.plot(stock_data["Close"])
plt.plot(sma, label="20-day SMA")
plt.legend()
plt.show()