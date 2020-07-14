#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        import math
        from collections import Counter
        counter = Counter(nums)
        return sum(math.comb(count, 2) for count in counter.values() if count > 1)
# @lc code=end

