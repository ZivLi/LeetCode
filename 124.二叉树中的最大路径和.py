#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(
                self.ans,
                max(l, 0) + max(r, 0) + node.val)
            return max(l, r, 0) + node.val
        dfs(root)
        return self.ans
# @lc code=end

