'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


'''
'''
Explanation

Use two pointers. Initalize a variable to hold the max profit
l = buy
r = sell
if while r is in bound - keep moving it til end of the array subtracting it from stocks[l] and keeping maxprofit var
if l is ever more than r 
l = r (because no profit to be made)

'''

def best_time_to_buy_sell_stock(stocks):

    l,r = 0, 1
    maxP = 0

    while r < len(stocks):
        if stocks[l] < stocks[r]:
            profit = stocks[r] - stocks[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP
