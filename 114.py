class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if not m or not n:
            return
        
        dp = [[0]*m for i in range(n)]
        
        for i in range(m):
            dp[-1][i] = 1
        for j in range(n):
            dp[j][-1] = 1
        dp[-1][-1] = 0
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[j][i] = dp[j+1][i] + dp[j][i+1]
        
        return dp[0][0]
        