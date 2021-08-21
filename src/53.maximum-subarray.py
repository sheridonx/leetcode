#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        in linear time
        """
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        cur_max = r =nums[0]
        ls_max = list()
        for num in nums[1:]:
            if num < 0:
                ls_max.append(cur_max)
            cur_max = max(num,cur_max + num)
        ls_max.append(cur_max)
        return max(ls_max)
# @lc code=end

if __name__ == "__main__":
    inputs = [
        [-2,1,-3,4,-1,2,1,-5,4],
        [-2,1]
    ]
    outputs = list()
    s = Solution()
    for nums in inputs:
        outputs.append(s.maxSubArray(nums))
    print(outputs)