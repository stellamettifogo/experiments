
def best_buy(prices):
    """ Returns the index of the best price to buy and sell. """
    prices_len = len(prices)
    # TODO write some great code here
    buy = 0
    sell = 0
    # loop esterno (buy)
    for i in range(0, prices_len - 1):
        # loop interno (sell)
        for j in range(i +1, prices_len):
            # if meglio, segna
            best_so_far = series[sell] - series[buy]
            best_now = series[j] - series[i]
            if best_now > best_so_far:
                buy = i 
                sell = j

    return buy, sell



# test series
series = [1, 2, 3, 4, 5]
buy1, sell1 = best_buy(series)
assert buy1 == 0 
assert sell1 == 4
# this string is formatted and tells the best time to buy and sell plus total gain
print(f"buy[{buy1}]: ${series[buy1]}, sell[{sell1}]: ${series[sell1]}, gain: ${series[sell1]-series[buy1]}")

# test series
series = [1, 2, 3, 4, 5, 3, 0]
buy, sell = best_buy(series)
assert buy == 0 
assert sell == 4
print(f"buy[{buy}]: ${series[buy]}, sell[{sell}]: ${series[sell]}, gain: ${series[sell]-series[buy]}")

# test series
series = [1, 2, 3, 0, 1, 5, 7, 8, 6, 2]
buy, sell = best_buy(series)
assert buy == 3 
assert sell == 7
print(f"buy[{buy}]: ${series[buy]}, sell[{sell}]: ${series[sell]}, gain: ${series[sell]-series[buy]}")



# regression testing
series = [5, 6, 7, 5, 4, 3, 2, 3, 4, 5, 6, 5, 4, 2, 0]
buy, sell = best_buy(series)
assert buy == 6 
assert sell == 10

print(f"buy[{buy}]: ${series[buy]}, sell[{sell}]: ${series[sell]}, gain: ${series[sell]-series[buy]}")

