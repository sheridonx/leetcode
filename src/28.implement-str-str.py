#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
# @lc code=end

if __name__ == "__main__":
    inputs = [
        ("hello","ll"),
        ("aaaaa","bba"),
        ("","asdfg"),
        ("qwfqff","")
    ]
    outputs = list()
    s = Solution()
    for h,n in inputs:
        outputs.append(s.strStr(h,n))
    print(outputs)