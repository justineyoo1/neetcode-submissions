class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_Count = {}
        t_Count = {}

        for char in s:
            s_Count[char] = s_Count.get(char, 0) + 1

        for char in t:
            t_Count[char] = t_Count.get(char, 0) + 1

        if s_Count == t_Count:
            return True
        return False
        