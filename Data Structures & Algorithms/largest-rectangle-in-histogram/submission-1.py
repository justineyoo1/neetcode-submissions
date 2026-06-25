class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n + 1):
            curBar = heights[i] if i < n else 0
            while len(stack) > 0 and curBar < heights[stack[-1]]:
                curHeight = heights[stack.pop()]
                if len(stack) == 0:
                    width = i
                else:
                    width = i - stack[-1] - 1
                curMax = curHeight * width
                maxArea = max(maxArea, curMax)
            stack.append(i)
        return maxArea 



            

        