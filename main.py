from functions import crosses_fun
from validticker import is_tradable

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
    stocks_list.append(str(input("tickers:")))

for ticker in stocks_list:
    if is_tradable(ticker):
        pass
    else:
        print("test")







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
