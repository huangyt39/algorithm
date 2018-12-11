class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return 
        
        num, count = 1.22, 0
        for i in nums:
            if i == num:
                count += 1
            else:
                if count >= 1:
                    count -= 1
                else:
                    num, count = i, 0
                    
        return num