#
# @lc app=leetcode.cn id=865 lang=python3
#
# [865] 具有所有最深节点的最小子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node, d):
            if not node: return (node, d)
            l, d_l = dfs(node.left, d+1)
            r, d_r = dfs(node.right, d+1)
            return l, d_l if d_l > d_r else r, d_r
        return dfs(root, -1)[0]
# @lc code=end

