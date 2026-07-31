class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = str(len(s))
            res += length + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = j + 1 + length
            word = s[start:end]
            res.append(word)
            i = end
        return res
        
            


