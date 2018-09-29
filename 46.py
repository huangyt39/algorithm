class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        max_res = 1
        count = 1
        nums.sort()
        res = nums[0]
        tmp = nums[0]
        for index in range(1, len(nums)):
          if nums[index] == tmp:
            count += 1
          else:
            if max_res < count:
              max_res = count
              res = tmp
            tmp = nums[index]
            count = 1
        if max_res < count:
          return tmp
        return res

A = [1,1,1,1,2,2,2]
print(Solution.majorityNumber(A, A))