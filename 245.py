"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # write your code here
        return self.isSubtreeWithFlag(T1, T2, 1)
        
    def isSubtreeWithFlag(self, T1, T2, flag):
        if flag:
            if not T2:
                return True
            if not T1:
                return False
        if not T2 and not T1:
            return True
        if not T2 or not T1:
            return False
        flag = 0
        
        if T1.val != T2.val:
            return self.isSubtreeWithFlag(T1.left, T2, flag) or self.isSubtreeWithFlag(T1.right, T2, flag)
        else:
            return self.isSubtreeWithFlag(T1.left, T2, flag) or self.isSubtreeWithFlag(T1.right, T2, flag) or (self.isSubtreeWithFlag(T1.left, T2.left, flag) and self.isSubtreeWithFlag(T1.right, T2.right, flag))