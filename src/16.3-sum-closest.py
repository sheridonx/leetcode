#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
import bisect
from typing import  List
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums = sorted(nums)
        r = sum(nums[:3])
        diff = abs(target-r)
        # return sum of the 3 smallest, nums if target is less than any num
        if target <= r:
            return r
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]+nums[i+2] > target:
                temp = nums[i]+nums[i+1]+nums[i+2]
                if abs(target-temp) < diff:
                    r = temp
                    diff = abs(target- temp)
                continue
            lc, rc = i+1, len(nums)-1
            while lc < rc:
                temp = nums[i] + nums[lc] + nums[rc]
                if abs(target-temp) < diff:
                    r = temp
                    diff = abs(target- temp)
                if temp < target:
                    lc += 1
                else:
                    rc -= 1
        return r             
# @lc code=end

inputs = [
    ([-1,2,1,-4],1),
    ([5,7,4,6,3],3),
    ([-100,-98,-2,-1],-101)
]
outputs = list()
s = Solution()
for nums,target in inputs:
    outputs.append(s.threeSumClosest(nums,target))
print(outputs)

