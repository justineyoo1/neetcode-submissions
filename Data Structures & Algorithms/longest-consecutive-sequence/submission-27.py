class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cleaned = set(nums)
        longest = 0

        for n in cleaned:
            # Only start counting if n is the beginning
            # of a consecutive sequence.
            if n - 1 not in cleaned:
                curMax = 1

                while n + curMax in cleaned:
                    curMax += 1

                longest = max(longest, curMax)

        return longest