class Solution:
    """
    @param n: An integer
    @return: An array storing 1 to the largest number with n digits.
    """
    def numbersByRecursion(self, n):
        # write your code here
        if n <= 0:
            return []
        if n == 1:
            return [i for i in range(10)][1:]
            
        n_1 = self.numbersByRecursion(n-1)
        if(n-1 == 1):
            n_1.insert(0,0)
        res = []
        for i in range(10):
            res += [i*(10**(n-1))]*(10**(n-1))
            for j in range(10**(n-1)):
                res[-j] += n_1[-j]
        
        return res[1:]