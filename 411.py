# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100
class Solution:
    """
    @param n: a number
    @return: Gray code
    """
    def grayCode(self, n):
        # write your code here
      res = [[0,0],[0,1],[1,1],[1,0]]
      res_ = []
      if n == 0:
        return [0]
      if n == 1:
        return [0, 1]
      while(n > 2):
        res_tmp = [arr[:] for arr in res]
        res_tmp.reverse()
        print(res)
        print(res_tmp)
        for arr in res:
          arr.insert(0, 0)
        print(res)
        print(res_tmp)
        for arr in res_tmp:
          arr.insert(0, 1)
          res.append(arr)
        n -= 1
        print(res)
      for num_arr in res:
        tmp = 1
        num = 0
        for index in num_arr[::-1]:
          num += tmp*index
          tmp *= 2
        res_.append(num)
      return res_

print(Solution.grayCode(2, 4))