class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                #this is the case becuase the key 
                #in dict is the value and the value is the index
                hashMap[n] = i