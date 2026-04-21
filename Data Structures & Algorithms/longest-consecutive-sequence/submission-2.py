class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #no dupes with hashset
        hashset = set(nums)
        longest = 1

        if not nums:
            return 0

        for n in nums:
            if n-1 not in hashset:
                cur = n
                curMax = 1
                while cur + 1 in hashset:
                    cur += 1
                    curMax += 1
                longest = max(longest, curMax)

        return longest
        
        
            



        
                

        
        