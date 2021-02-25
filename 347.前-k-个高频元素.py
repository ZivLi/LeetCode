#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count_d = sorted(Counter(nums).items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        return [i for i, _ in count_d][:k]

# @lc code=end

