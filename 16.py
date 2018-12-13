class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
        
        if len(nums) == 1:
            return [[nums[0]]]
        subsets = self.permuteUnique(nums[1:])
        res = []
        for subset in subsets:
            for i in range(len(subset)+1):
                tmp = subset[:]
                tmp.insert(i, nums[0])
                if tmp not in res:
                    res.append(tmp)
        return res