#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
# Given an integer, convert it to a roman numeral. 
# Input is guaranteed to be within the range from 1 to 3999.
#

# @lc code=start
class Solution:
    roman_ele = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
     }
    roman_subt_cases = {
        'M': [],
        'C': ['D','M'],
        'X': ['L','C'],
        'I': ['V', 'X']
    }
    def intToRoman(self, num: int) -> str:
        r = ''
        reste = num
        for c, ls_subt in self.roman_subt_cases.items():
            v = self.roman_ele[c]
            temp = int(reste / v)
            temp_c = ''
            if temp == 9:
                temp_c = c + ls_subt[1]
            elif temp > 5:
                temp_c = ls_subt[0] + (temp-5)*c
            elif temp == 5:
                temp_c = ls_subt[0]
            elif temp == 4:
                temp_c = c + ls_subt[0]
            elif temp > 0:
                temp_c = temp * c
            r += temp_c
            reste -= temp * v
        return r
# @lc code=end

if __name__ == "__main__":
    inputs = [
        3,
        4,
        9,
        58,
        1994
    ]
    outputs = list()
    s = Solution()
    for input in inputs:
        outputs.append(s.intToRoman(input))
    print(outputs)