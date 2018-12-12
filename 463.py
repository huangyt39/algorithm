class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if not A:
            return
        
        for i in range(len(A)):
            change = False
            for j in range(len(A)-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]
                    change = True
            if not change:
                return
        
        return