import yfinance as yf
import pandas as pd

def crosses_fun(stock_choice):
    df = yf.download(stock_choice, period="2y")

    df["ma50"] = df["Close"].rolling(window=50).mean()
    df["ma200"] = df["Close"].rolling(window=200).mean()

    last_50 = df["ma50"].iloc[-1]
    last_200 = df["ma200"].iloc[-1]

    if last_50 > last_200:
        return "gold"
    elif last_200 > last_50:
        return "dead"
    else:
        print("waow")











