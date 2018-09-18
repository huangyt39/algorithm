class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
      d = {}
      for num in A:
        if num in d:
          del d[num]
        else:
          d[num] = 1
      return d.keys()

A = [1,5,-1,1,2,2,3,4,4,5,3,2147483647,8,9,9,8]
print(Solution.singleNumberIII(A, A))