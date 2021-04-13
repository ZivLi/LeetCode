#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
        return ans
# @lc code=end

