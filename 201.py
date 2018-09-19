"""
Definition of SegmentTreeNode:
"""
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        else:
            root.left = Solution.build(start, start, (start + end)//2)
            root.right = Solution.build(start, (start + end)//2 + 1, end)
            return root