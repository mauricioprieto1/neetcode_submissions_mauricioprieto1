class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for unsortedString in strs:
            sortedS = ''.join(sorted(unsortedString))
            res[sortedS].append(unsortedString)

        return list(res.values())
        