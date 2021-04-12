#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        def compare(a, b):
            return int(a+b) - int(b+a)
        nums = sorted(map(str,nums), key=functools.cmp_to_key(compare))
        return ''.join(nums)
# @lc code=end

