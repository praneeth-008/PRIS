import yfinance as yf 

tickers = ["AAPL", "MSFT", "JPM", "XOM", "JNJ", "WMT"]

data = yf.download(tickers, start= "2024-01-01", end= "2026-01-01", auto_adjust=True)

price = data["Close"]

returns = price.pct_change()

print(returns.head)