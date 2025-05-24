# https://leetcode.com/problems/find-words-containing-character/submissions/1642738469/?envType=daily-question&envId=2025-05-24

class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        return [i for i, word in enumerate(words) if x in word]   
        