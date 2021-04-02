#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            else:
                sl, pl = dfs(root.left)
                sr, pr = dfs(root.right)
                return sl+sr+root.val, abs(sl-sr)+pl+pr
        _, ans = dfs(root)
        return ans
# @lc code=end

