class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid
        return min(nums[right], nums[left])

print(Solution.findMin(1, [4,5,6,7,0,1,2]))