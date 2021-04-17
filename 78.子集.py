#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for a in ans:
                ans = ans + [a + [num]]
        #         res = [[]]
        # for i in nums:
        #     res = res + [[i] + num for num in res]
        return ans
# @lc code=end

