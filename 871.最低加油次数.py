#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations += [(target, 0)]
        cur = startFuel
        ans = 0

        h = []
        last = 0
        for i, fuel in stations:
            cur -= i - last
            while cur < 0 and h:
                cur -= heapq.heappop(h)
                ans += 1
            if cur < 0:
                return -1
            heappush(h, -fuel)

            last = i
        return ans
# @lc code=end

