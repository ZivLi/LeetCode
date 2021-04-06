#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return False
            l = dfs(node.left)
            r = dfs(node.right)
            if not l: node.left=None
            if not r: node.right=None
            return node.val==1 or l or r
        return root if dfs(root) else None
        
# @lc code=end

