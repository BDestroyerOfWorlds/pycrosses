from selectors import SelectSelector

from functions import crosses_fun
from validticker import is_tradeable

stocks_list = []
golden_list = []
dead_list = []

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
        stocks_list.append(ticker_for_trial)
    else:
        print(f"{ticker_for_trial} is invalid or delisted")

#need to make up my mind about what im gonna do from this point

for ticker in stocks_list:

    if crosses_fun(ticker) == "dead":
        dead_list.append(ticker)
    elif crosses_fun(ticker) == "gold":
        golden_list.append(ticker)
    else :
        pass

print("dead list")
print(dead_list)
print("golden list")
print(golden_list)
