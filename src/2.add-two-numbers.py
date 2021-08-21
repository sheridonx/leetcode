#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.32%)
# Likes:    7887
# Dislikes: 2018
# Total Accepted:    1.4M
# Total Submissions: 4.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        ptr = l
        tmp = 0
        while True:
            if l1 is not None:
                tmp += l1.val
                l1 = l1.next
            if l2 is not None:
                tmp += l2.val
                l2 = l2.next
            tmp,v = divmod(tmp,10)
            ptr.val = v
            if tmp==0 and l1 is None and l2 is None:
                return l
            # there should be a ListNode pointed by the current one
            new_ln = ListNode(0)
            ptr.next = new_ln
            ptr = new_ln
# @lc code=end

if __name__ == '__main__':
    l1_3 = ListNode(3)
    l1_2 = ListNode(4,next=l1_3)
    l1_1 = ListNode(2,next=l1_2)
    l2_3 = ListNode(4)
    l2_2 = ListNode(6,next=l2_3)
    l2_1 = ListNode(5,next=l2_2)

    s = Solution()
    ln = s.addTwoNumbers(l1_1,l2_1)
    while ln is not None:
        print(ln.val)
        ln = ln.next

    l1_2 = ListNode(8)
    l1_1 = ListNode(0,next=l1_2)
    l2_3 = ListNode(4)
    l2_2 = ListNode(6,next=l2_3)
    l2_1 = ListNode(5,next=l2_2)

    s = Solution()
    ln = s.addTwoNumbers(l1_1,l2_1)
    while ln is not None:
        print(ln.val)
        ln = ln.next