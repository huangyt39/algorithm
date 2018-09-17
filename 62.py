class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if len(A) == 0:
          return -1
        if len(A) == 1:
          if A[0] == target:
            return 0
          else:
            return -1
        index = 0
        while index != len(A) - 1 and A[index] < A[index + 1]:
          index += 1
        #print(index)
        head = index + 1
        tail = index
        if index == len(A) - 1:
          head = 0
          tail = index
         
        while head != tail:
          #print(head, tail)
          if head < tail:
            mid = (head + tail)//2
            if A[mid] < target:
              head = mid + 1
            elif A[mid] > target:
              tail = mid - 1
            else:
              return mid
          else:
            mid = ((head + tail + len(A))//2)%len(A)
            if A[mid] < target:
              head = mid
            elif A[mid] > target:
              tail = mid
            else:
              return mid
        if A[head] != target:
          return -1
        else:
          return head

A = [1001,10001,10007,1,10,101,201]
target = 10001
print(Solution.search(A, A, target))