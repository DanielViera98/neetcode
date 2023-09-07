#You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to 
#maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
#to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Find max & min
        #if min ind < max ind, return. Otherwise, del max, try again

        while (len(prices) > 0):
            mSell = max(prices)
            mBuy = min(prices)
            if prices.index(mBuy) < prices.index(mSell):
                return mSell-mBuy
            else:
                del prices[prices.index(mBuy)]
        return 0


'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #calc max - first
        #remove first
        #restart
        maxProfit = 0
        while len(prices) > 1:
            mSell = max(prices)
            if mSell - prices[0] > maxProfit:
                maxProfit = mSell-prices[0]
            #print(prices, mSell, prices[0], maxProfit)
            del prices[0]
            
        return maxProfit     
'''

#First Attempt
#Thought Process: Set min to first objec
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]                      #Set buy price to first item
        maxSell = prices[1]                     #Set Sell Price to second item
        for i in range(1, len(prices)-1):       #Iterate from 1 to prices length -1
            if prices[i] < minBuy:
                minBuy = prices[i]
            if prices[i] > maxSell:
                maxSell = prices[i]
            print(minBuy, maxSell)
        if minBuy < maxSell:
            return maxSell-minBuy
        else:
            return 0
'''
#Problems: No check for array length, so if prices length is less than 2 it will throw an error.