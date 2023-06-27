import yfinance as yf
from sklearn.linear_model import LinearRegression


# 1. get data
ix_ticker = '^GSPC ^KS11'
data = yf.download(ix_ticker, start="2011-01-01", end="2029-04-30")

# 2. 데이타 정제
data.dropna(inplace=True)  # 편의를 위해서 둘 다 존재하는 날만 이용
col = [f'{i[1]}_{i[0]}' for i in data.columns]
data = data.droplevel(0, axis=1)
data.columns = col
y = data['^KS11_Close'].iloc[1:]
col2 = ['^GSPC_Close', '^GSPC_High', '^GSPC_Low', '^GSPC_Open', '^GSPC_Volume', ]
x = data[col2].shift(1).dropna()

# 3. Create a Linear Regression model and fit it to the data
model = LinearRegression()
model.fit(x, y)

# 4. Use the model to make predictions about future prices
future_prices = model.predict(x)

# 5. 예측 가격이 더 높으면 매수, 낮으면 매도
p = (1 * (future_prices > y) - 1 * (future_prices < y)).shift(1) * (y.diff())
p.cumsum().plot()