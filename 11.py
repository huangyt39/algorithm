"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    def printself(self):
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
        print("print: ", arr)

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        res = []
        if root == None: return res
        Solution.searchDown(res, root, k1, k2, res)
        ls = list(res)
        ls.sort(reverse = False)
        return ls

    def searchDown(self, root, k1, k2, res):
        if root.val >= k1 and root.val <= k2:
            res.append(root.val)
            if root.left != None:
                Solution.searchDown(root.left, root.left, k1, k2, res)
            if root.right != None:
                Solution.searchDown(root.right, root.right, k1, k2, res)
        elif root.val < k1 and root.right != None:
            Solution.searchDown(root.right, root.right, k1, k2, res)
        elif root.val > k2 and root.left != None:
            Solution.searchDown(root.left, root.left, k1, k2, res)
        return

testroot = TreeNode(20)
testroot.left = TreeNode(8)
testroot.right = TreeNode(22)
testroot.left.left = TreeNode(4)
testroot.left.right = TreeNode(12)
testroot.printself()
print(Solution.searchRange(testroot, testroot, 10, 22))