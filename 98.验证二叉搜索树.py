#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= pre:
            return False

        pre = root.val
        return self.isValidBST(root.right)
# @lc code=end

