def maxProfit(prices):
    maxProfit = 0
    buy = prices[0]
    for price in prices[1:]:
        print(maxProfit)
        if price<buy:
            buy = price
        elif price-buy> maxProfit:
            maxProfit = price-buy
    return maxProfit

print(maxProfit([10,20,30,15,50,25]))#10 --> 30 -10 = 20  (5+(35), 15)
