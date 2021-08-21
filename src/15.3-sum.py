#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
import bisect
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        if len(nums) < 3:
            return res
        dict_count = dict()
        for num in nums:
            if num not in dict_count:
                dict_count[num] = 1
            else:
                dict_count[num] += 1
        nums = sorted(dict_count)
        for v in nums:
            if v == 0:
                if dict_count[v]>2:
                    res.add((0,0,0))
            elif dict_count[v] > 1 and -2*v in dict_count:
                res.add((v,v,-2*v))
            if v < 0:
                target = -v
                left = min(bisect.bisect_right(nums,v),len(nums)-1)
                right = min(bisect.bisect_left(nums,target-v),len(nums)-1)
                while left < right:
                    if nums[left] + nums[right] == target:
                        res.add((v,nums[left],nums[right]))
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -=1
        return res
# @lc code=end
