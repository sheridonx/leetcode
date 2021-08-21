#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List
# @lc code=start
class Solution:
    dc_mapping = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }
    def letterCombinations(self, digits: str) -> List[str]:
        r = list()
        for d in digits:
            if len(r) == 0:
                r = self.dc_mapping[d]
            else:
                r = [p+n for p in r for n in self.dc_mapping[d]]
        return r
# @lc code=end

inputs = [
    '23',
    '456',
    '45322'
]
outputs = list()
s = Solution()
for input in inputs:
    outputs.append(s.letterCombinations(input))
print(outputs)