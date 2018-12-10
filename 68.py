"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        res = []
        stack1 = []
        stack2 = []
        stack1.append(root)
        
        while stack1:
            node = stack1.pop()
            if node:
                stack1.append(node.left)
                stack1.append(node.right)
                stack2.append(node.val)
                
        while stack2:
            res.append(stack2.pop())
        return res