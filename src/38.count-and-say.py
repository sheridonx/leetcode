#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==0:
            return ''
        if n==1: 
            return '1'
        previous_r = self.countAndSay(n-1)
        ls_count = list()
        pre_caract = None
        count = 0
        for d in previous_r:
            if d == pre_caract:
                count += 1
            else:
                if pre_caract:
                    ls_count.append((pre_caract,count))
                pre_caract = d
                count = 1
        ls_count.append((pre_caract,count))
        r = ''
        for d,c in ls_count:
            r += str(c) + d
        return r
# @lc code=end


if __name__ == "__main__":
    inputs = [
        1,
        2,
        3,
        4,
        5
    ]
    outputs = list()
    s = Solution()
    for n in inputs:
        outputs.append(s.countAndSay(n))
    print(outputs)