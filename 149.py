class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) <= 1:
          return 0
        max_pro = 0
        min_pri = 99999
        for num in prices:
          min_pri = min(min_pri, num)
          max_pro = max(max_pro, num - min_pri)
        return max_pro
