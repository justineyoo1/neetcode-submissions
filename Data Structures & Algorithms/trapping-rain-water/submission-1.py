class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L = 0
        R = n - 1
        res = 0

        lHeight = height[L]
        rHeight = height[R]

        while L < R:
            if height[L] < height[R]:
                L += 1
                lHeight = max(height[L], lHeight)
                res += lHeight - height[L]
            else:
                R -= 1
                rHeight = max(height[R], rHeight)
                res += rHeight - height[R]
        return res 

        