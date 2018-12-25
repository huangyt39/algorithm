class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 
        
        # dp[i,j] = triangle[i,j] + min(dp[i+1,j], dp[i+1,j+1])
        m = len(triangle)
        dp = [[0]*m for i in range(m)]
        
        dp[-1][:] = triangle[-1][:]
        for i in range(m-2, -1, -1):
            for j in range(i, -1, -1):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]