#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            r = int('-'+str(x)[1:][::-1])
        else:
            r = int(str(x)[::-1])
        if r>2**31-1 or r<-2**31:
            return 0
        return r

# @lc code=end

s = Solution()
a = s.reverse(1534236469)
b = s.reverse(1563847412)
c = s.reverse(-123)
d = s.reverse(1024)
e = s.reverse(10240)
pass