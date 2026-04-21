class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)

        for word in strs:
            s = [0] * 26
            for char in word:
                s[ord(char) - ord('a')] += 1
            answer[tuple(s)].append(word)
        
        return list(answer.values())

        
        