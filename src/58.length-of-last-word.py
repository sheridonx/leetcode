#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
# @lc code=end


if __name__ == "__main__":
    inputs = [
        '',
        'a         ',
        'a ',
        'afsd qwrqafasfqaw'
    ]
    outputs = list()
    s = Solution()
    for n in inputs:
        outputs.append(s.lengthOfLastWord(n))
    print(outputs)