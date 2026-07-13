from functions import crosses_fun

stocks_list = []
golden_list = []
dead_list = []

number_of_stocks = int(input("number of tickers: "))

for i in range(number_of_stocks):
    stocks_list.append(input("tickers:"))

for ticker in stocks_list:

    if crosses_fun(ticker) == "sell":
        dead_list.append(ticker)
    elif crosses_fun(ticker) == "buy":
        golden_list.append(ticker)
    else :
        pass

print("dead list")
print(dead_list)
print("golden list")
print(golden_list)