class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n == 0:
            return 1
        if n < 3:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            
            dp[i] = dp[i-1] * 2
            for j in range(2, i):
                dp[i] += (dp[j-1] * dp[i-j])
        
        return dp[n]
                
        
        
