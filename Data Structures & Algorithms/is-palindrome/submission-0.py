class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #get rid of spaces and upper
        cleaned = "".join(c for c in s if c.isalnum()).lower()

        L = 0
        R = len(cleaned) - 1

        while L < R:
            if cleaned[L] != cleaned[R]:
                return False
            else:
                L += 1
                R -= 1   

        return True     