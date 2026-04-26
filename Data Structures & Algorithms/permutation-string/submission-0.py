class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        windowSize = len(s1)

        val_s1 = Counter(s1)


        for i in range(len(s2)):
            window = s2[i : i + windowSize]
            windowFreqMap = Counter(window)

            if windowFreqMap == val_s1:
                return True
            
        return False


            




        
        