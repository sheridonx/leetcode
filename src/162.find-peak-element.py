#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from typing import List
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lc, rc = 0,len(nums)-1
        while lc < rc-1:
            m = (lc+rc)//2
            if nums[m] > nums[m+1] and nums[m]>nums[m-1]:
                return m
            elif nums[m] < nums[m+1]:
                lc = m+1
            else:
                rc = m-1
        return rc if nums[rc]>nums[lc] else lc
# @lc code=end

inputs = [
    [1],
    [1,2],
    [2,1],
    [1,2,3,1],
    [1,2,1,3,5,6,4],
    [1,2,3,4,5,6]
]
outputs = list()
s = Solution()
for input in inputs:
    outputs.append(s.findPeakElement(input))
print(outputs)