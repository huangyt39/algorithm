"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if head == None or n < 0:
            return head
        
        lf, rg = head, head
        for i in range(n):
            rg = rg.next
            
        if rg == None:
            delNode = head
            head = head.next
            del delNode
            return head
            
        while rg.next != None:
            rg = rg.next
            lf = lf.next
        
        delNode = lf.next
        lf.next = delNode.next
        del delNode
        return head