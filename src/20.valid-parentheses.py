#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (38.52%)
# Likes:    4713
# Dislikes: 211
# Total Accepted:    961.5K
# Total Submissions: 2.5M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start

class Solution:
    buskets = {
    '(':')',
    '[':']',
    '{':'}'
    }

    def isValid(self, s: str) -> bool:
        q = list()
        if len(s)%2 == 1:
            return False
        for c in s:
            if c in self.buskets:
                q.append(c)
            else:
                if len(q)==0 or c != self.buskets[q.pop()]:
                    return False
        if len(q)==0:
            return True
# @lc code=end

inputs = [
    "(",
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "){",
    "))"
]
outputs = list()
s = Solution()
for test_input in inputs:
    outputs.append(s.isValid(test_input))
print(outputs)
