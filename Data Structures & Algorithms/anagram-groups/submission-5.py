class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        anagram share the same frequency array
        [0]*26

        res = {
        freqArray : ["","",""]
        }

        1. iterate over the list of strings 
            build freqArray for each string
                [0] * 26 
                get ascii value of the char, to use as index
            add to dict {freqArray : ["",""]}
        2. return dict.values()
        """
        res = defaultdict(list) 
        for string in strs:

            freqArray = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                freqArray[index] += 1
            freqArray = tuple(freqArray)
            res[freqArray].append(string)
        return list(res.values())
