#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
                
# @lc code=end

if __name__ == "__main__":
    inputs = [
        ([3,2,2,3], 3),
        ([],1),
        ([1,2,35,1],1),
        ([1,2,2341,435],7)
    ]
    outputs = list()
    s = Solution()
    for nums,val in inputs:
        outputs.append(s.removeElement(nums,val))

    print(outputs)