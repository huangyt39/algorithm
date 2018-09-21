"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    def __str__(self):
        stack = []
        arr = []
        stack.append(self)
        while len(stack) != 0:
            if stack[0] != '#':
                arr.append(stack[0].val)
                if stack[0].left == None:
                    stack.append('#')
                else :
                    stack.append(stack[0].left)
                if stack[0].right == None:
                    stack.append('#')
                else :
                    stack.append(stack[0].right)
            else: arr.append('#')
            stack.pop(0)
        return " ".join(' %s' %id for id in arr)

class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if len(preorder) != len(inorder):
            return None
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index = 0
        for index in range(len(inorder)):
            if inorder[index] == preorder[0]:
                break
        leftlen = index
        rightlen = len(inorder) - index - 1
        print(preorder[1:leftlen + 1], inorder[:index])
        print(preorder[-rightlen:], inorder[index + 1:])
        root.left = Solution.buildTree(1, preorder[1:index + 1], inorder[:index])
        root.right = Solution.buildTree(1, preorder[1 + index - len(inorder):], inorder[index + 1:])
        return root

A = [2, 3]
B = [3, 2]
print(Solution.buildTree(A, A, B))