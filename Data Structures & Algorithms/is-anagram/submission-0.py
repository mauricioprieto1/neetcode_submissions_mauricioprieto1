class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = ''.join(sorted(s))
        st = ''.join(sorted(t))
        if ss == st:
            return True 
        else:
            return False 