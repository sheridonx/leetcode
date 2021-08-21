#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        s,b = divmod(len(nums),2)
        if b==0:
            return (nums[s-1] + nums[s])/2
        else:
            return nums[s]

# @lc code=end
