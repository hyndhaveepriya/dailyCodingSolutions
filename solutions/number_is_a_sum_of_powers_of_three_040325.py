#https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/submissions/1562290065/?envType=daily-question&envId=2025-03-04

class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True
        