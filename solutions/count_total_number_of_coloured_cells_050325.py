#https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05

class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 + 2 * (n - 1) * n

        