import yfinance as yf
from yfinance import ticker


def is_tradable(ticker):
    checked_ticker = yf.Ticker(ticker)
    checked_info = checked_ticker.info

    return checked_info.get("tradeable") or checked_info.get("cryptoTradeable")

print(is_tradable(ticker))