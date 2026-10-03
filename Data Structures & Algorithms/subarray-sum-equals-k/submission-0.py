class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #would be to in a prefix sum methoer, calc cumSum
        #then in parrallel i would also count freq of values of the previous cumSUm, 
        #calc diff, and if diff value had a count then add that to res

        res = 0
        cumSum = 0
        prefixSum = {0: 1}


        for n in nums:
            cumSum += n
            diff = cumSum - k
            res += prefixSum.get(diff, 0)

            prefixSum[cumSum] = prefixSum.get(cumSum, 0) + 1


        return res

        
        