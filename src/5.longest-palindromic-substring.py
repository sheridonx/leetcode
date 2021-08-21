#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2: return s
        if s == s[::-1]: return s
        r = ''
        for i in range(len(s)):
            a = self._extend_palindrome(i,i,s)
            b = self._extend_palindrome(i,i+1,s)
            if len(a) > len(r) : r = a
            if len(b) > len(r) : r = b
        return r

    def _extend_palindrome(self,i,j,s):
        while i >= 0 and j < len(s) and s[i]==s[j]:
            i -= 1
            j += 1
        return s[i+1:j]

# @lc code=end

if __name__ == '__main__':
    inputs  = [
        "aba",
        "babad",
        "cbbd",
        "pwwkew",
        "a",
        "au",
        "dvdf",
        "bacabacab",
        "ccd"
    ]
    outputs = list()
    s = Solution()
    for ip in inputs:
        outputs.append(s.longestPalindrome(ip))
    print(outputs)