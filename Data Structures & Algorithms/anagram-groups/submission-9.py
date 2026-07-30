class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for strings in strs:
            count = [0] * 26
            for char in strings:
                idx = ord(char) - ord('a')
                count[idx] += 1
            results[tuple(count)].append(strings)

        return list(results.values())
        