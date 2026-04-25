class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_freqMap = {}
        t_freqMap = {}

        for char in s:
            s_freqMap[char] = 1 + s_freqMap.get(char, 0)

        for char in t:
            t_freqMap[char] = 1 + t_freqMap.get(char, 0)

        if s_freqMap == t_freqMap:
            return True
        return False





        
        
        