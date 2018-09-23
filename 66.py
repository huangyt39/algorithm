"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if root == None:
          return []
        # write your code here
        arr = []
        stack = []
        stack.append(root)
        tmp = root
        while len(stack) != 0:
          tmp = stack[-1]
          arr.append(tmp.val)
          stack.pop()
          if tmp.right:
            stack.append(tmp.right)
          if tmp.left:
            stack.append(tmp.left)
        return arr


