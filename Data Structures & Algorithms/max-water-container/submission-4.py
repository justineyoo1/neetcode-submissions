class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxVol = 0

        L = 0
        R = len(heights) - 1

        while L < R:

            curVol = min(heights[L], heights[R]) * (R - L)
            maxVol = max(maxVol, curVol)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return maxVol


        
        