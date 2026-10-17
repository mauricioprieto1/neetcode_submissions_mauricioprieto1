class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach:
            1. array of length 26 to store each str's char count 
            2. dict with key= 26 length array, value=list of strs
            3. iterate over the strs and store each str's array into the dict
            4. return the dict.values()

        """
        
        wordsDict = defaultdict(list)

        for string in strs:
            key = [0 for i in range(26)]

            for character in string:
                index = ord(character) - ord('a')
                key[index] += 1
            key = tuple(key)
            wordsDict[key].append(string)
        
        return list(wordsDict.values())