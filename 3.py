class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, n, k):
        # write your code here
        result = 0
        if(k == 0): result += 1
        for i in range(int(n + 1)):
          while i > 0:
            if i % 10 == k:
              result += 1
            i //= 10
        return result

print(Solution.digitCounts(1, 19, 0))

