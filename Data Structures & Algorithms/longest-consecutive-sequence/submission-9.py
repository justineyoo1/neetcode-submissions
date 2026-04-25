class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #no dupes with hashset
        hashset = set(nums)
        longest = 1

        if len(nums) == 0:
            return 0

        for n in nums:
            if n - 1 not in hashset:
                cur = n
                curMax = 1
                while cur + 1 in hashset:
                    curMax += 1
                    cur += 1
                longest = max(curMax, longest)

        return longest
                


        
        
            



        
                

        
        