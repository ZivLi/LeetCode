class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = {}
        for n in nums:
            if n not in l:
                l[n] = 1
            else:
                del l[n]
        return l.keys()[0]
        """
        Another brilliant answer.
        """
        # return sum(set(nums))*2 - sum(nums)*2
