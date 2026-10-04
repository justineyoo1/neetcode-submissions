class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        maxArea = 0

        while L < R:
            curArea = (R - L) * min(heights[L], heights[R])
            maxArea = max(curArea, maxArea)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return maxArea
            

        