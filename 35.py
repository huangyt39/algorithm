"""
Definition of ListNode

"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
        pointTo = None
        while head != None and head.next != None:
            Sec = head.next
            nextHead = Sec.next
            Sec.next = head
            head.next = pointTo
            head = nextHead
            pointTo = Sec
        if head == None:
            return pointTo
        else:
            head.next = pointTo
            return head
        
l1 = ListNode(1)
l2 = ListNode(2, l1)
l3 = ListNode(3, l2)
l4 = ListNode(4, l3)
l5 = ListNode(5, l4)

tmp = Solution.reverse(1, l5)
while tmp != None:
    print(tmp.val, "->")
    tmp = tmp.next