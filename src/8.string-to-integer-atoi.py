#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        d_str = ''
        for c in str.strip():
            if c.isdigit():
                d_str += c
            elif len(d_str)==0 and c in ['-','+']:
                d_str += c
            else:
                break
        try:
            r = int(d_str)
        except:
            r = 0
        if r < -2**31:
            r = -2**31
        elif r > 2**31-1:
            r = 2**31-1
        return r
# @lc code=end

if __name__ == "__main__":
    inputs = [
        "  -0012a42",
        "4193 with words",
        "   -42",
        "words and 987",
        "-91283472332",
        "91283472332",
        "3.1415",
        "+1"
    ]
    outputs = list()
    s = Solution()
    for input in inputs:
        outputs.append(s.myAtoi(input))
    print(outputs)