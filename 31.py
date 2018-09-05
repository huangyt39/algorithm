class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0:
          return 0
        if len(nums) == 1:
          if nums[0] >= k:
            return 1
          else: return 0
        else:
          i = 0
          j = len(nums) - 1
          while True:
            while i != j and nums[j] >= k:
              j -= 1
            if i == j:
              break
            while i != j and nums[i] < k:
              i += 1
            if i == j:
              break
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
          print(nums)
          for index, num in enumerate(nums):
            if num >= k:
              return index
          return len(nums)

A = [7,7,9,8,6,6,8,7,9,8,6,6]
k = 10
print(Solution.partitionArray(A, A, k))