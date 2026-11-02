class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sets = set(s)
        sett = set(t)

        return sets == sett






        # l = 0
        # r = len(t)
        # for _ in range(len(s)):
            