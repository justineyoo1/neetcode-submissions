class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        
        for s in strs:
            state = [0] * 26
            for char in s:
                idx = ord('a') - ord(char)
                state[idx] += 1
            freqMap[tuple(state)].append(s)
        
        return list(freqMap.values())
            

        