
#https://leetcode.com/problems/find-missing-and-repeated-values/submissions/1564560599/?envType=daily-question&envId=2025-03-06


class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        total_sum = (n * n * (n * n + 1)) // 2
        total_sum_squares = (n * n * (n * n + 1) * (2 * n * n + 1)) // 6
        sum_actual = 0
        sum_actual_sq = 0
        for row in grid:
            for num in row:
                sum_actual += num
                sum_actual_sq += num * num
        diff_sum = total_sum - sum_actual  
        diff_sum_squares = total_sum_squares - sum_actual_sq
        sum_ab = diff_sum_squares // diff_sum
        a = (diff_sum + sum_ab) // 2
        b = a - diff_sum  
        return [b, a]
        