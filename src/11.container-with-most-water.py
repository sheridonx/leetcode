#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lc, rc = 0, len(height)-1
        max_height = max(height)
        r = (rc-lc) * min(height[lc],height[rc])
        while lc < rc:
            # end loop if no larger container is possible
            if max_height * (rc-lc) < r:
                break
            # move to the larger container
            if height[lc]< height[rc]:
                lc += 1
            else:
                rc -= 1
            temp = (rc-lc) * min(height[lc],height[rc])
            if temp > r:
                r = temp
        return r
# @lc code=end

if __name__ == "__main__":
    inputs = [
        [1,8,6,2,5,4,8,3,7],
        [9,8,4,3,1,5,6,7,9],
        [1,3,2,5,25,24,5]
    ]
    outputs = list()
    s = Solution()
    for input in inputs:
        outputs.append(s.maxArea(input))
    print(outputs)