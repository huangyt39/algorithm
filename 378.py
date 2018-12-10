"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        listRoot = self.bstToList(root)[0]
        # while listRoot and listRoot.prev :
        #     listRoot = listRoot.prev
        return listRoot
        
    def bstToList(self, root):    
        if not root:
            return None, None
        
        listRoot = DoublyListNode(root.val)
        listRoot.prev = self.bstToList(root.left)[1]
        if listRoot.prev:
            listRoot.prev.next = listRoot
        listRoot.next = self.bstToList(root.right)[0]
        if listRoot.next:
            listRoot.next.prev = listRoot
        
        first, last = listRoot,listRoot
        while first.prev:
            first = first.prev
        while last.next:
            last = last.next
        return first, last
        