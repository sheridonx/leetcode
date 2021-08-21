#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
         return bin(int(a,2)+int(b,2))[2:]
# @lc code=end

if __name__ == "__main__":
    inputs = [
        ['11','1'],
        ['1010','1011']
    ]
    outputs = list()
    s = Solution()
    for (a,b) in inputs:
        outputs.append(s.addBinary(a,b))
    print(outputs)
