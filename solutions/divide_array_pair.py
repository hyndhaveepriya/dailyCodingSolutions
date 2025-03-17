#https://leetcode.com/problems/divide-array-into-equal-pairs/submissions/1576941607/?envType=daily-question&envId=2025-03-17

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        for value in count.values():
            if value % 2 != 0:
                return False
        
        return True
        