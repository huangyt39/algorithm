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
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        if not head:
            return 
        
        newHead = ListNode(1)
        newTmp = newHead
        unSort = head
        while unSort:
            minNode = unSort
            tmp = unSort
            while tmp:
                if tmp.val <= minNode.val:
                    minNode = tmp
                tmp = tmp.next
            minNode.val, unSort.val = unSort.val, minNode.val
            tmp = unSort
            unSort = unSort.next
            
            newTmp.next = tmp
            newTmp = newTmp.next
            
        return newHead.next