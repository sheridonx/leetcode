#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
from typing import List
# @lc code=start
class Solution:
    def find_n_sum(self, nums, target, n, result, results):
        if len(nums) < n or n < 2: return

        # solve 2-sum
        if n == 2:


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
# @lc code=end

inputs = [
    ([1,0,-1,0,-2,2],0),
]
outputs = list()
s = Solution()
for ls, targer in inputs:
    outputs.append(s.fourSum(ls,target))
print(outputs)