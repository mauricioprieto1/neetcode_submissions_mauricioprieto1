class Solution:

    def encode(self, strs: List[str]) -> str:
        # length # <str> length # <str>
        res = ''
        for s in strs:
            length = len(s)
            res += f'{length}#{s}'
        return res
    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < len(s):
            if s[r] == '#':
                length = int(s[l:r])
                currentString = s[r + 1 : r + 1 + length]
                res.append(currentString)
                l = r + 1 + length
                r = r + 1 + length
            else:
                r += 1
        return res