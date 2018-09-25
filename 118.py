class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """

    def numDistinct(self, S, T):
        # write your code here
        # i = len(S), j = len(T)
        # if S[-1] != T[-1] dp[i][j] = dp[i - 1][j]
        # else dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        if T == "":
          return 1
        arr = [[0]*(len(T) + 1) for row in range(len(S) + 1)]
        for i in range(len(S) + 1):
          arr[i][0] = 1
        for i in range(1, len(S) + 1):
          for j in range(1, len(T) + 1):
            if S[i-1] != T[j-1]:
              arr[i][j] = arr[i - 1][j]
            else:
              arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
          #print(arr)
        return arr[-1][-1]

S = 'rabbbit'
T = 'rabbit'
print(Solution.numDistinct(S, S, T))