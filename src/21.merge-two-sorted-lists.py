#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode()
        ptr = r
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            if l1.val > l2.val:
                ptr.val = l2.val
                l2 = l2.next
            else:
                ptr.val = l1.val
                l1 = l1.next
            ptr.next = ListNode()
            ptr = ptr.next
        l = l1 if l1 else l2
        ptr.val = l.val
        while l.next:
            l = l.next
            ptr.next = ListNode(l.val)
            ptr = ptr.next
        return r
# @lc code=end