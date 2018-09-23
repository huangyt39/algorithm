 """
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root == None:
          return True
        res = []
        res = Solution.midTraverse(root, root, res)
        for i in range(len(res) - 1):
          if res[i] >= res[i + 1]:
            return False
        return True
        
    def midTraverse(self, root, res_arr):
      if root == None:
        return res_arr
      res_arr = Solution.midTraverse(root, root.left, res_arr)
      res_arr.append(root.val)
      res_arr = Solution.midTraverse(root, root.right, res_arr)
      return res_arr