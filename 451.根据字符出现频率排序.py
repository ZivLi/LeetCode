#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        count_d = Counter(s)
        sorted_count = sorted(count_d.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        return ''.join([e[0]*e[1] for e in sorted_count])
# @lc code=end

