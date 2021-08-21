#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        set_tree = set(root)
        if None in set_tree:
            if len(set_tree) == 2:
                return 
# @lc code=end

inputs = [
    [1,1,1,1,1,None,1],
    [2,2,2,5,2],
]
outputs = list()
s = Solution()
for input in inputs:
    outputs.append(s.isUnivalTree(input))
print(outputs)