#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, current, p1 = 0, 0, len(nums) - 1
        while current <= p1:
            if nums[current] == 0:
                nums[current], nums[p0] = nums[p0], nums[current]
                p0 += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[p1] = nums[p1], nums[current]
                p1 -= 1
            else:
                current += 1
        return nums

# @lc code=end

