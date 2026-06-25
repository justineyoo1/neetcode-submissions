class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        maximum = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            else:
                curMax = prices[R] - prices[L]
                maximum = max(maximum, curMax)
        return maximum 


        
