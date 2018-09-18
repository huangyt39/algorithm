class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumberII(self, A):
        # write your code here
      arr = [0] * 32
      for num in A:
        #print(num, arr)
        for index in range(-1, -32, -1):
          temp = (num & 1)
          arr[index] += temp
          arr[index] %= 3
          num = num >>1
      res = 0
      for j in range(32):
        res += arr[31 - j]*pow(2, j)
      return res

A = [1,1,2,3,3,3,2,2,4,1]
print(Solution.singleNumberII(A, A))