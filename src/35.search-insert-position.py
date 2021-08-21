#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
import bisect
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums,target)
# @lc code=end


if __name__ == "__main__":
    inputs = [
        ([1,2,3,4], 3),
        ([0,2,3],1),
        ([1,2,35,234],77),
        ([1,2,234,435],7123),
        ([],99)
    ]
    outputs = list()
    s = Solution()
    for nums,val in inputs:
        outputs.append(s.searchInsert(nums,val))

    print(outputs)