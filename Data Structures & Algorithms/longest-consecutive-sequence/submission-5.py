class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #order doesn't matter, as long as n+1 is in there, it should increase longest +1

        hashset = set(nums)
        #default, atleast 1
        longest = 1

        if len(nums) == 0:
            return 0


        for n in nums:
            if n - 1 not in hashset:
                cur = n
                curMax = 1
                while cur + 1 in hashset:
                    cur += 1
                    curMax += 1
                longest = max(longest, curMax)

        return longest
                    


        
        
            



        
                

        
        