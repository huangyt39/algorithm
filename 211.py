class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here 
        if not A and not B:
            return True
        if not A or not B:
            return False
        if len(A) != len(B):
            return False
        
        dicA = {}
        for a in A:
            if not a in dicA:
                dicA[a] = 0
            else:
                dicA[a] += 1
        
        dicB = {}
        for b in B:
            if not b in dicB:
                dicB[b] = 0
            else:
                dicB[b] += 1
            
        for key, val in dicA.items():
            if key in dicB:
                if dicB[key] != val:
                    return False
            else:
                return False
            
        return True