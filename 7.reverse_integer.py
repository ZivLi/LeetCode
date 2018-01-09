class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        res = int(y[::-1]) if not y.startswith('-') else 0 - int(y[-1:0:-1])
        return 0 if abs(res) > (2 ** 31 - 1) else res
