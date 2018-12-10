"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        res = []
        self.binaryTreePath(root, target, [], res)
        
        return res
        
    def binaryTreePath(self, root, target, arr, res):
        if not root:
            return
        
        target -= root.val
        arr.append(root.val)
        if target == 0 and (not root.left and not root.right):
            res.append(arr)
            return
        else:
            self.binaryTreePath(root.left, target, arr[:], res)
            self.binaryTreePath(root.right, target, arr[:], res)
            return 