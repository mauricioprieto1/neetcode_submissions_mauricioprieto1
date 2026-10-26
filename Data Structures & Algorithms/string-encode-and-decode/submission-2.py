class Solution:

    def encode(self, strs: List[str]) -> str:
        # length # <str> length # <str>
        res = []
        for s in strs:
            length = len(s)
            res.append(f'{length}#{s}')
        return ''.join(res) # optimization instead of doing string += newWord O(n^2) -> O(n)
    def decode(self, s: str) -> List[str]:
        l = r = 0 # chained assingment
        res = []
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                currentString = s[r + 1 : r + 1 + length]
                res.append(currentString)
                l = r = r + 1 + length
            else:
                r += 1
        return res
    # O(N) time
    # O(N) space