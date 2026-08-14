class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        profit=0
        sell=1
        while sell<len(prices):
            if prices[buy]>prices[sell]:
                buy=sell
                sell+=1
            else:
                tempprofit=prices[sell]-prices[buy]
                profit=max(profit,tempprofit)
                sell+=1
        return profit
