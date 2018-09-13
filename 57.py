class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
      res = []
      bthanzero,sthanzero = [], []
      zerocount = 0
      for num in numbers:
        if num >= 0:
          bthanzero.append(num)
          if num == 0:
            zerocount += 1
        else :
          sthanzero.append(num)
      if zerocount >= 3:
        res.append([0, 0, 0])
      #x1,x2>=0 x3<0
      for x3 in sthanzero:
        #print("x3: ",x3)
        for x1 in bthanzero:
          b2 = bthanzero[:]
          b2.remove(x1)
          for x2 in b2:
            if x1 + x2 + x3 == 0:
              if x1 > x2:
                if [x3, x2, x1] not in res:
                  res.append([x3, x2, x1])
              else :
                if [x3, x1, x2] not in res:
                  res.append([x3, x1, x2])
      #...
      for x3 in bthanzero:
          for x1 in sthanzero:
            s2 = sthanzero[:]
            s2.remove(x1)
            for x2 in s2:
              if x1 + x2 + x3 == 0:
                if x1 > x2:
                  if [x2, x1, x3] not in res:
                    res.append([x2, x1, x3])
                else :
                  if [x1, x2, x3] not in res:
                    res.append([x1, x2, x3])
      return res


A = [1,2,33,23,2423,33,23,1,7,6,8787,5,33,2,3,-23,-54,-67,100,400,-407,-500,-35,-8,0,0,7,6,0,1,2,-56,-89]
print(Solution.threeSum(A, A))