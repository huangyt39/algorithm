class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]
        
        if len(nums) == 1:
            return [[nums[0]],[]]
        nums.sort(reverse=True)
        res = []
        subsets = self.subsetsWithDup(nums[1:])
        for subset in subsets:
            res.append(subset)
        for subset in subsets:
            tmp = subset[:]
            tmp.append(nums[0])
            if tmp not in res:    
                res.append(tmp)
        return res
    