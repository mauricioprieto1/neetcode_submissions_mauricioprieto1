class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        same amount of characters, two strings
        """
        if len(s) != len(t):
            return False 
        for char in s:
            if char not in t:
                return False
        return True

    