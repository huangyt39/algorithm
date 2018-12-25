class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        
        dp = [0]*len(A)
        dp[0] = A[0]
        for i in range(1, len(A)):
            if dp[i-1] >= i:
                dp[i] = max(dp[i-1], A[i]+i)
        
        return dp[-1] >= len(A)-1