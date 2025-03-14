#https://leetcode.com/problems/maximum-candies-allocated-to-k-children/submissions/1573909359/?envType=daily-question&envId=2025-03-14

class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def canDistribute(x):
            total_children = 0
            for candy in candies:
                total_children += candy // x
                if total_children >= k: 
                    return True
            return total_children >= k
        left, right = 1, max(candies)
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                best = mid  
                left = mid + 1
            else:
                right = mid - 1
        
        return best