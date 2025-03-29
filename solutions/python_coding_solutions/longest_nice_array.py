#https://leetcode.com/problems/longest-nice-subarray/submissions/1589877256/?envType=daily-question&envId=2025-03-18

class Solution(object):
    def longestNiceSubarray(self, nums):
        n = len(nums)
        start = 0
        current_or = 0
        max_len = 0
        
        for end in range(n):
            while current_or & nums[end] != 0:
                current_or ^= nums[start]
                start += 1
            
            current_or |= nums[end]
            max_len = max(max_len, end - start + 1)
        
        return max_len
