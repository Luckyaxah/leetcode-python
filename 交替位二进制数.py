class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = n ^ (n >> 1)
        return temp & (temp + 1) == 0

