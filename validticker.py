import yfinance as yf


def is_tradeable(spam):

    spam_ticker = yf.Ticker(spam)
    spam_ticker_info = spam_ticker.info
    print(spam_ticker_info)

    return spam_ticker_info.get("hasPrePostMarketData")

