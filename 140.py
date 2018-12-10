class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        # (x1 + x2)**n == x1**n + x1**(n-1)*x2 + ... + x2**n
        # a**n = (x1*b + x2)**n
        # a**n % b = x2**n % b
        return self.Power(a,b,n,1)
    
    def Power(self, a, b, n, m):
        if a >= b:
            return self.Power(a%b, b, n, m)
        else:
            if a <= 1 or n <= 1:
                return (a**n*m)%b
            if n%2 == 0:
                return self.Power(a**2, b, n//2, m)
            else:
                return self.Power(a**2, b, n//2, m*a)
                
                # 3751 9723 2723 4713 