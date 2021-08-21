#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        strs.sort()
        r=''
        for a,b in zip(strs[0],strs[-1]):
            if a!=b: return r
            r += a
        return r

# @lc code=end

inputs = [
    ["flower","flow","flight"],
    ["dog","racecar","car"],
    ["c","c"],
    ['a'],
    ["aa","aa"],
    ["aa",""],
    ["aaa","aa","aaa"]
]
outputs = list()
s = Solution()
for test_input in inputs:
    outputs.append(s.longestCommonPrefix(test_input))
print(outputs)
