
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
            best_so_far = prices[sell] - prices[buy]
            best_now = prices[j] - prices[i]
            if best_now > best_so_far:
                buy = i 
                sell = j

    return buy, sell



datasets = [
    {
        "series": [5, 6, 7, 5, 4, 3, 2, 3, 4, 5, 6, 5, 4, 2, 0],
        "buy": 6,
        "sell": 10
    },
    {
        "series": [1, 2, 3, 0, 1, 5, 7, 8, 6, 2],
        "buy": 3,
        "sell": 7
    },
    {
        "series": [1, 2, 3, 4, 5, 3, 0],
        "buy": 0,
        "sell": 4
    },
    {
        "series": [1, 2, 3, 4, 5],
        "buy": 0,
        "sell": 4
    }
]

for data in datasets:
    rbuy, rsell = best_buy(data["series"])
    assert rbuy == data["buy"]
    assert rsell == data["sell"]
    print(f"series: {data['series']}")
    print(f"buy[{rbuy}]: ${data['series'][rbuy]}")
    print(f"sell[{rsell}]: ${data['series'][rsell]}")
    print(f"gain: ${data['series'][rsell] - data['series'][rbuy]}\n\n")
