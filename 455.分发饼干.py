#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        cnt = 0
        for i in range(len(s)):
            if s[i] >= g[cnt]:
                cnt += 1
            if cnt == len(g):
                return cnt
        return cnt
# @lc code=end

