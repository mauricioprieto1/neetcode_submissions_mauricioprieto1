class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            abc = [0] * 26
            for c in string:
                abc[ord(c) - ord('a')] += 1
            res[tuple(abc)].append(string)
        return list(res.values())