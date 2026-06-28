class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        L = 0
        maxCount = 0
        maxLen = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxCount = max(maxCount, count[s[R]])
            if (R - L + 1) - maxCount > k:
                count[s[L]] -= 1
                L += 1
            maxLen = max(maxLen, R - L + 1)

        return maxLen
                
        