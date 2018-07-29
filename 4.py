class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
      list = [1]
      if n == 1: return 1;
      for num in range(n - 1):
        for i in list:
          if i*2 > list[-1]:
            min2 = i*2
            break
        for i in list:
          if i*3 > list[-1]:
            min3 = i*3
            break
        for i in list:
          if i*5 > list[-1]:
            min5 = i*5
            break
        list.append(min(min2, min3, min5))
      return list[-1]

print(Solution.nthUglyNumber(9, 9));