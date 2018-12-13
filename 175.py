"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if not root:
            return
        
        tmp = root
        stack = []
        stack.append(tmp)
        while stack:
            item = stack.pop()
            item.right, item.left = item.left, item.right
            if item.left:
                stack.append(item.left)
            if item.right:
                stack.append(item.right)
        return
    
    # def invertBinaryTree(self, root):
    #     # write your code here
    #     if not root:
    #         return
        
    #     root.left, root.right = root.right, root.left
    #     self.invertBinaryTree(root.left)
    #     self.invertBinaryTree(root.right)
        
    #     return