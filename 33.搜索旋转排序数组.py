#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
            # 基于二分查找的变形
        array = nums
        if not array:
            return -1
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid

            # 左半段有序
            if array[mid] >= array[left]:
                if array[left] <= target <= array[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半段有序
            else:
                if array[mid] <= target <= array[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# @lc code=end

