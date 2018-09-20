class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
      if len(nums) == 0:
        return [[]]
      if len(nums) == 2:
        res = [nums[1], nums[0]]
        return [res, nums]
      res = []
      for i in nums:
        sub_nums = []
        for num in nums :
          if num != i:
            sub_nums.append(num)
        for arr in Solution.permute(sub_nums, sub_nums):
          sub_arr = []
          sub_arr.append(i)
          for num in arr:
            sub_arr.append(num)
          res.append(sub_arr)
      return res

A = [0, 1]
print(Solution.permute(A, A))