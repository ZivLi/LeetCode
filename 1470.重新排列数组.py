#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend([nums[i], nums[i + n]])
        return res
# @lc code=end

