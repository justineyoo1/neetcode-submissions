class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 1

        if len(nums) == 0:
            return 0

        for n in nums:
            if n - 1 not in hashset:
                cur = n
                curMax = 1
                for n in hashset:
                    if cur+1 in hashset:
                        cur += 1
                        curMax += 1
                longest = max(longest, curMax)
        return longest