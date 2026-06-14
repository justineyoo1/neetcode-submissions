class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L = 0
        R = len(heights) - 1
        maximum = 0

        while L < R:
            #calculate,
            minHeight = min(heights[L], heights[R])
            curMax = minHeight * (R - L)
            maximum = max(maximum, curMax)
            if heights[L] == heights[R]:
                L += 1
            elif heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maximum

            
        