#https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/submissions/1604568505/?envType=daily-question&envId=2025-04-02


class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        n = len(nums)

       
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    
                    value = (nums[i] - nums[j]) * nums[k]
                    
                    
                    max_value = max(max_value, value)

        return max_value
