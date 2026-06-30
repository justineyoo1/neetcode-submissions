class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxLen = 0
        L = 0
        res = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            maxLen = max(maxLen, count[s[R]])
            if (R - L + 1 - maxLen) > k:
                count[s[L]] -= 1
                L += 1
                
            res = max(res, R - L + 1)
        return res
        
        
                
        