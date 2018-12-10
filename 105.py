"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        if not head.next:
            return RandomListNode(head.label)
            
        tmp = head
        while tmp:
            coptmp = RandomListNode(tmp.label)
            coptmp.next = tmp.next
            tmp.next = coptmp
            tmp = coptmp.next
            
        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
            
        tmp = head
        tmp2 = head.next
        newHead = tmp.next
        while tmp:
            tmp.next = tmp2.next
            if tmp.next:
                tmp2.next = tmp.next.next
            else:
                break
            tmp = tmp.next
            tmp2 = tmp2.next
        
        return newHead