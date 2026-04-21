class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyPoint = float('inf')
        curProf = 0
        maxProf = 0

        for price in prices:
            if price < buyPoint:
                buyPoint = price
            
            curProf = price - buyPoint
            maxProf = max(curProf, maxProf)
        return maxProf


        
