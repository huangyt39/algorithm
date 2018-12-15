class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if not A:
            return 0
        
        return self.findIndex(A, target, 0, len(A))
        
    def findIndex(self, A, target, lf, rg):
        if lf < rg:
            mid = (rg-lf)//2 + lf
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                return self.findIndex(A, target, mid+1, rg)
            else:
                return self.findIndex(A, target, lf, mid)
        if lf == rg:
            return lf