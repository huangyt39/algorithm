class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_res = -999999
        tmp = 0
        sortednum = nums[:]
        sortednum.sort()
        if sortednum[-1] <= 0:
            return sortednum[-1]
        for i in nums:
            tmp += i
            if tmp < 0:
                tmp = 0
            max_res = max(tmp, max_res)
        return max_res

print(Solution.maxSubArray(1, [-1,-2,-3,-100,-1,-50]))