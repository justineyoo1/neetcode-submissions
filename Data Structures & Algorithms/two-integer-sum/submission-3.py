class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}


        #enumerate
        #diff comes first because it's 
        #already stored in hashmap so it came before

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[n] = i