#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        r_parts = [''] * numRows
        ptr = 0
        direction = -1
        for c in s:
            r_parts[ptr] += c
            if ptr==0 or ptr == numRows-1:
                direction = -1 * direction
            ptr += direction
        return ''.join(r_parts)
            
# @lc code=end

if __name__ == '__main__':
    inputs  = [
        ("PAYPALISHIRING",3),
        ("PAYPALISHIRING",4),
        ("AB",1)
    ]
    outputs = list()
    s = Solution()
    for st,num in inputs:
        outputs.append(s.convert(st,num))
    print(outputs)
