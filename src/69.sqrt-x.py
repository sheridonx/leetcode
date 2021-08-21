#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))
# @lc code=end

if __name__ == "__main__":
    inputs = [
        9,
        8,
        4
    ]
    outputs = list()
    s = Solution()
    for input in inputs:
        outputs.append(s.mySqrt(input))
    print(outputs)

