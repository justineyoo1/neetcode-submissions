class Solution:
    def isPalindrome(self, s: str) -> bool:


        #clean up the string: no space no non alphanumerics (abc, 123)

        filtered = ""
        for char in s:
            if char.isalnum() == True:
                filtered += char.lower()
        

        L = 0
        R = len(filtered) - 1

        while L < R:
            if filtered[L] != filtered[R]:
                return False
            else:
                L += 1
                R -= 1
        return True



        