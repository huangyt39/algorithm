class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
      res = []
      nums.sort()
      res.append(nums)
      index = 0
      while index < len(res):
        if len(res[index]) == 1:
          index += 1
          continue
        arr = res[index]
        for num in arr:
          tmp = []
          for i in arr:
            if i != num:
              tmp.append(i)
              if len(tmp) <= 2:
                tmp.sort()
          if tmp not in res:
            res.append(tmp)
        index += 1
      if [] not in res:
        res.append([])
      res.sort()
      return res

A = [4, 1, 0]
print(Solution.subsets(A, A))