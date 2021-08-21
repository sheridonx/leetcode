#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
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
        'I': ['V','X'],
        'X': ['L','C'],
        'C': ['D','M'],
    }

    def romanToInt(self, s: str) -> int:
        r = 0
        previous_letter = None
        for l in s:
            if previous_letter in self.roman_subt_cases:
                if l in self.roman_subt_cases[previous_letter]:
                    r -= 2* self.roman_ele[previous_letter]
            r += self.roman_ele[l]
            previous_letter = l
        return r

# @lc code=end
inputs = ["III","IV","IX","LVIII","MCMXCIV"]
outputs = list()
s = Solution()
for test_input in inputs:
    outputs.append(s.romanToInt(test_input))
print(outputs)
