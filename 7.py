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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        res = []
        if root == None: return res
        stack = []
        stack.append(root)
        while(len(stack) != 0):
            if stack[0] != None:
                res.append(stack[0].val)
                stack.append(stack[0].left)
                stack.append(stack[0].right)
            else:
                res.append('#')
            stack.pop(0)
        return res

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        stack = []
        left = True
        if len(data) == 0: return None
        else:
            root = TreeNode(data[0])
            stack.append(root)
        index = 1
        while len(stack) != 0 and index < len(data): 
            if data[index] == '#':
                if left:
                    left = False
                else:
                    stack.pop(0)
                    left = True
            else:
                if left:
                    stack[0].left = TreeNode(data[index])
                    stack.append(stack[0].left)
                    left = False
                else:
                    stack[0].right = TreeNode(data[index])
                    stack.append(stack[0].right)
                    left = True
                    stack.pop(0)
            index += 1
        return root

testroot = TreeNode(3)
testroot.left = TreeNode(9)
testroot.right = TreeNode(20)
testroot.right.left = TreeNode(15)
testroot.right.right = TreeNode(7)
testroot.printself()
print(Solution.serialize(testroot, testroot))
testarr = [3, 9, 20, '#', '#', 15, 7]
resroot = Solution.deserialize(testarr, testarr)
resroot.printself()
