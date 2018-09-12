class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        # write you code here
        if x%7 == 3: return "YES"
        else: 
          tmp = x%7
          while(tmp <=21):
            x -= 7
            tmp += 7
            if tmp%3 == 0 and x >= 0:
              return "YES"
          return "NO"

print(Solution.isBuild(345,345))