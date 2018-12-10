class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if len(nums) <= 1:
            return 
        
        start, end = 0, len(nums)-1
        while start < end:
            while nums[start]%2 == 1:
                start += 1
            while nums[end]%2 == 0:
                end -= 1
            if start >= end:
                return
            else:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
        return
            