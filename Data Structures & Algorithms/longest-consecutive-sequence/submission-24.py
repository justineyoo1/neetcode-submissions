class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet= set(nums)
        longest = 1

        if len(nums) == 0:
            return 0

        for n in nums:
            if n - 1 not in hashSet:
                cur = n
                curMax = 1
                while n + curMax in hashSet:
                    curMax += 1
                longest = max(longest, curMax)
        return longest        