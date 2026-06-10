class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_Count = {}
        t_Count = {}

        for char in s:
            s_Count[char] = 1 + s_Count.get(char, 0) 

        for char in t:
            t_Count[char] = 1 + t_Count.get(char, 0)

        return s_Count == t_Count 






        
        
        