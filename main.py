from functions import crosses_fun
from validticker import is_tradeable
import time

stocks_set = set()
golden_set = set()
dead_set = set()

#numbers block
def ticker_number():
    while True:
        try:
            ticker_amount = int(input("number of tickers: "))
            if ticker_amount <= 0:
                raise ValueError
            else:
                return ticker_amount

        except ValueError:
            print("please insert a positive integer")

for i in range(ticker_number()):
    ticker_for_trial = str(input("tickers:"))
    if is_tradeable(ticker_for_trial):
        stocks_set.add(ticker_for_trial)
    else:
        print(f"{ticker_for_trial} is invalid or delisted")

#adding block

while True:
    try:
        for ticker in stocks_set:
            if crosses_fun(ticker) == "dead":
                dead_set.add(ticker)
            elif crosses_fun(ticker) == "gold":
                golden_set.add(ticker)
            else:
                pass

            print("dead list")
            print(dead_set)
            print("golden list")
            print(golden_set)

            time.sleep(86400)
    except:

        print("error")

        continue

print("dead list")
print(dead_set)
print("golden list")
print(golden_set)
