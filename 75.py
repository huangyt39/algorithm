import time

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
      index = len(A)//2
      move = index // 2
      while True:
        #print(index)
        #time.sleep(1)
        if A[index] > A[index + 1] and A[index] > A[index - 1]:
          return index
        elif A[index] > A[index + 1] and A[index] < A[index - 1]:
          index -= move
          if move == 0:
            index -= 1
        elif A[index] < A[index + 1] and A[index] > A[index - 1]:
          index += move
          if move == 0:
            index += 1
        else :
          index -= move
        move //= 2

B = [1, 2, 1]
A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,15,14,13,12,11,10,9,8,7,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,46,45,44,43,42,41,40,39,40,41,42,43,44,45,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
print(Solution.findPeak(A, A))