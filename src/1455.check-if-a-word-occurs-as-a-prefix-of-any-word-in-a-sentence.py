#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        r = -1
        for i,w in enumerate(words):
            if w.startswith(searchWord):
                return i+1
        return r
# @lc code=end

if __name__ == "__main__":
    inputs = [
        ("i love eating burger","burg"),
        ("this problem is an easy problem","pro"),
        ("i am tired", "you"),
        ("i use triple pillow","pill"),
        ("hello from the other side","they")
    ]
    outputs = list()
    s = Solution()
    for st,w in inputs:
        outputs.append(s.isPrefixOfWord(st,w))
    print(outputs)