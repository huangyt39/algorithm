"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if not root:
            return 
        
        # findA -> from parent of A go up to find B
        pathToA = self.findVal(root, A.val)
        for parent in pathToA:
            if self.findVal(parent, B.val):
                return parent
        
    def findVal(self, root, A):
        if not root:
            return
        res = []
        if root.val == A:
            return [root]
        reslf = self.findVal(root.left, A)
        resrg = self.findVal(root.right, A)
        if reslf:
            res = reslf
            res.append(root)
        if resrg:
            res = resrg
            res.append(root)
        return res