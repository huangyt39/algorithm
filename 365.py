class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        count = 0
        if num >= 0:
            while num != 0:
                count += num%2
                num = num >> 1 
            return count
        else:
            return Solution.countOnes(1, 2**32 + num)

print(Solution.countOnes(1, -178))