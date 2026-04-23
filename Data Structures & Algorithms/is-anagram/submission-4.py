class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_freqMap = {}
        t_freqMap = {}


        for n in s:
            s_freqMap[n] = 1 + s_freqMap.get(n, 0)

        for n in t:
            t_freqMap[n] = 1 + t_freqMap.get(n, 0)

        if s_freqMap == t_freqMap:
            return True
        else:
            return False
            



        
        
        