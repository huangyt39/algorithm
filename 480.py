"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
            
        res = []
        if not root.left and not root.right:
            return [str(root.val)]
        reslf = self.binaryTreePaths(root.left)
        resrg = self.binaryTreePaths(root.right)
        for item in reslf:
            res.append(str(root.val)+'->'+item)
        for item in resrg:
            res.append(str(root.val)+'->'+item)
        
        return res