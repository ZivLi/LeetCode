#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right, cnt = 0, 1, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1

# @lc code=end

