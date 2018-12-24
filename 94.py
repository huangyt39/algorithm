"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        if not root:
            return 0
            
        arr = []
        res = self.findPath(root, arr)
        if arr:
            arr.sort()
            arrMax = arr[-1]
            return max(arrMax, res)
        return res
        
    def findPath(self, root, arr):
        if not root:
            return -999
        
        lf, rg = self.findPath(root.left, arr), self.findPath(root.right, arr)
        
        res = max(lf+root.val, rg+root.val, root.val)
        if rg+lf+root.val > res:
            arr.append(rg+lf+root.val)
        if lf > res:
            arr.append(lf)
        if rg > res:
            arr.append(rg)
        
        return res