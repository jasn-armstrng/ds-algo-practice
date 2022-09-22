# Question: Best Time to Buy and Sell Stock
# Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# O(n^2) solution below too slow for very large inputs.
def maxProfit(prices=[])->int:
    mp=0
    days=len(prices)

    for i in range(0,days-1): # O(n) *
        for j in range(i+1, days): # O(n)
            # O(1)
            sale=prices[j]-prices[i]
            if sale>mp:
                mp=sale

    return mp

# To do:
# O(n) solution

if __name__=="__main__":
    # Test cases and expected output
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices)) # -> 5
    prices = [7,2,8,3,5,1]
    print(maxProfit(prices)) # -> 6
    prices = [7,6,4,3,1]
    print(maxProfit(prices)) # -> 0
    prices = [7,6,4,1,1]
    print(maxProfit(prices)) # -> 0
    prices = [7,6,4,1,1,10]
    print(maxProfit(prices)) # -> 9
    prices = [7,1]
    print(maxProfit(prices)) # -> 0
    prices = [1]
    print(maxProfit(prices)) # -> 0
    prices = [3,2,6,5,0,3]
    print(maxProfit(prices)) # -> 4
    prices = [0]
    print(maxProfit(prices)) # -> 0
    prices = [2,1,2,0,1]
    print(maxProfit(prices)) # -> 1
