class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        stack, res = [], []
        tmp = root
        while stack or tmp:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            if stack:
                item = stack.pop()
                res.append(item.val)
                tmp = item.right
        
        return res