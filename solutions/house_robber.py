#https://leetcode.com/problems/house-robber-iv/submissions/1574134515/?envType=daily-question&envId=2025-03-15

class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canRobWithCapability(cap):
            count, last_robbed = 0, -2 
            for i in range(len(nums)):
                if nums[i] <= cap and i > last_robbed + 1:
                    count += 1
                    last_robbed = i
                if count >= k:  
                    return True
            return count >= k
        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if canRobWithCapability(mid):
                high = mid 
            else:
                low = mid + 1  

        return low
        