class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maximum = 0

        
        while i < j:

            lower_height = min(heights[i], heights[j])
            diff = j - i
            maximum = max(maximum, lower_height * diff)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -=1
        return maximum

        
            
        