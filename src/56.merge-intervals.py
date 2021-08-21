#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
# @lc code=end

if __name__ == "__main__":
    inputs = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]]
    ]
    outputs = list()
    s = Solution()
    for input in inputs:
        outputs.append(s.merge(input))
    print(outputs)
