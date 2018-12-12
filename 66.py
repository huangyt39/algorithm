class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if not root:
            return []
        
        res, stack = [], []
        stack.append(root)
        while stack:
            item = stack.pop()
            res.append(item.val)
            if item.right:
                stack.append(item.right)
            if item.left:
                stack.append(item.left)
        
        return res