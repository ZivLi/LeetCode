#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lidx, ridx = 0, len(numbers)-1
        while lidx <= ridx:
            if numbers[lidx] + numbers[ridx] > target:
                ridx -= 1
            elif numbers[lidx] + numbers[ridx] < target:
                lidx += 1
            else:
                return [lidx+1, ridx+1]
# @lc code=end

