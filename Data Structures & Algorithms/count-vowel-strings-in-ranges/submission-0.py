class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        #1) Identify whether or not string starts/ends with a vowel
        vowel = set('aeiou')
        prefixSum = [0] * (len(words) + 1)

        prev = 0
        for i, wrd in enumerate(words):
            if wrd[0] in vowel and wrd[-1] in vowel:
                prev += 1
            prefixSum[i + 1] = prev
                
        #2) Querying and Returning
        queryRes = [0] * len(queries)

        for i, (l, r) in enumerate(queries):
            queryRes[i] = prefixSum[r + 1] - prefixSum[l]

        return queryRes
        