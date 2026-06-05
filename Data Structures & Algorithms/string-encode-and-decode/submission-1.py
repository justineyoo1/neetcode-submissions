class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += "~" + word

        return res


    def decode(self, s: str) -> List[str]:

        res = []
        currWord = ""
        
        if len(s) == 0:
            return res

        for i in range(1, len(s)):
            if s[i] != "~":
                currWord += s[i]
            else:
                res.append(currWord)
                currWord = ""

        res.append(currWord)

        return res
            


        
