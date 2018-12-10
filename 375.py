"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if not root:
            return None
        
        newRoot = TreeNode(root.val)
        newRoot.left = self.cloneTree(root.left)
        newRoot.right = self.cloneTree(root.right)
        
        return newRoot