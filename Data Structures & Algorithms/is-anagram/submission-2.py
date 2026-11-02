class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        same amount of characters, two strings
        """
        for char in s:
            if char not in t:
                return False
        return True

    