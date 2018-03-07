class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(map(S.count, J))
