"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head == None:
          return False
        slow = head
        fast = head.next
        while fast != None:
          slow = slow.next
          fast = fast.next
          if fast == slow:
            return True
          if fast and fast.next:
            fast = fast.next
        return False