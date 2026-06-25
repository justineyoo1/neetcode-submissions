class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L = 0
        R = n - 1

        lMax = height[L]
        rMax = height[R]

        res = 0

        while L < R:
            if height[L] < height[R]:
                L += 1
                lMax = max(lMax, height[L])
                res += lMax - height[L]
            else:
                R -= 1
                rMax = max(rMax, height[R])
                res += rMax - height[R]
        return res
        