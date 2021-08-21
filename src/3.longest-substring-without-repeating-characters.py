#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        r = ''
        temp = ''
        for c in s:
            if c not in temp:
                temp += c
            else:
                if len(temp)>len(r):
                    r = temp
                temp = temp.split(c)[-1] + c
        return max(len(r),len(temp))
# @lc code=end

if __name__ == '__main__':
    inputs  = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "a",
        "au",
        "dvdf"
    ]
    outputs = list()
    s = Solution()
    for ip in inputs:
        outputs.append(s.lengthOfLongestSubstring(ip))
    print(outputs)