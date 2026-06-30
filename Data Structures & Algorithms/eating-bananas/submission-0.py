class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        ans = R

        while L <= R:
            total = 0
            mid = (L + R) // 2
            for p in piles:
                total += math.ceil(p / mid)
            if total <= h:
                ans = mid
                R = mid - 1
            else:
                L = mid + 1
        return ans

        