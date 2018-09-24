"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        res = ""
        tmp = self
        while tmp != None:
          res += str(tmp.val)
          res += " -> "
          tmp = tmp.next
        res += "None"
        return res

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def Middle(self, head):
        slow, fast = head, head.next
        while fast != None:
          slow = slow.next
          fast = fast.next
          if fast:
            fast = fast.next
        return slow

    def Merge(self, head1, head2):
        if head1 == None:
          return head2
        if head2 == None:
          return head1
        # if head1.val < head2.val:
        #   left = head1
        #   right = head2
        # else:
        #   left = head2
        #   right = head1

        # while right != None:
        #   tmp = left.next
        #   insert = left
        #   while tmp != None and tmp.val < right.val:
        #     tmp = tmp.next
        #     insert = insert.next
        #   rightnext = right.next
        #   inserttmp = insert.next
        #   insert.next = right
        #   right.next = inserttmp
        #   right = rightnext
        # return left
        if head1.val < head2.val:
          head1.next = Solution.Merge(head1, head1.next, head2)
          return head1
        else:
          head2.next = Solution.Merge(head1, head1, head2.next)
          return head2

    def sortList(self, head):
        # write your code here
        if head == None or head.next == None:
          return head
        if head.next.next == None:
          if head.val > head.next.val:
            tmp = head.next
            head.next.next = head
            head.next = None
            return tmp
          return head
        mid = Solution.Middle(head, head)
        right = Solution.sortList(mid.next, mid.next)
        mid.next = None
        left = Solution.sortList(head, head)
        return Solution.Merge(left, left, right)

l3 = ListNode(-2)
l2 = ListNode(-1, l3)
l1 = ListNode(1, l2)
print(l1)
print(Solution.sortList(l1, l1))