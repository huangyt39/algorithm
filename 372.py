"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: the node in the list should be deletedt
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if node == None:
            return
        
        nextnode = node.next
        if nextnode == None:
            node = None
        else:
            tmp = nextnode
            node.val = nextnode.val
            node.next = nextnode.next
            del tmp
        return