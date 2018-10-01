class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) <= 1:
            return 0
        prices.reverse()
        print(prices)
        res = 0
        tmppri = prices[0]
        for i in range(len(prices) - 1):
            if tmppri > prices[i + 1]:
                res += (tmppri - prices[i + 1])
                tmppri = prices[i + 1]
            else:
                tmppri = prices[i + 1]
        return res
            
print(Solution.maxProfit(1, [2,1,2,0,1]))