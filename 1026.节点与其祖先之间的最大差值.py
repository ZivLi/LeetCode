#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxvalue = 0
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.dfs(root,0,100001)
        return self.maxvalue

    def dfs(self,node,maxv,minv):
        if not node:
            self.maxvalue = max(maxv-minv, self.maxvalue)
        else:
            maxv, minv = max(maxv,node.val), min(minv,node.val)
            self.dfs(node.left,maxv,minv)
            self.dfs(node.right,maxv,minv)

# @lc code=end

