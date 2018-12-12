class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        if not A or not m:
            return 0
        
        bag = [0]*(m+1)
        
        for i in A:
            for j in range(m, -1, -1):
                if j >= i:
                    bag[j] = max(bag[j], bag[j-i]+i)
        
        return bag[m] 
        
# m = 10, A = [3,4,8,5]
# A[i] == 3:
# [0,0,0,3,3,3,3,3,3,3,3]
# A[i] = 4:
# [0,0,0,3,4,4,4,7,7,7,7]
# A[i] == 8:
# [0,0,0,3,4,4,4,7,7,7,7]
# A[i] == 5:
# [0,0,0,3,4,5,5,7,8,9,9]