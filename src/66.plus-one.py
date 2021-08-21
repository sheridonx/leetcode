#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = [int(s) for s in str(int(''.join(str(d) for d in digits))+1)]
        return r
# @lc code=end

if __name__ == "__main__":
    inputs = [
        [1,2,3],
        [4,3,2,2],
        [1,5,7,9,9,9],
        [9,9,9]
    ]
    outputs = list()
    s = Solution()
    for input in inputs:
        outputs.append(s.plusOne(input))
    print(outputs)