class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cumSum = 0
        prefixCount = {0: 1}

        for n in nums:
            cumSum += n

            diff = cumSum - k

            res += prefixCount.get(diff, 0)

            prefixCount[cumSum] = prefixCount.get(cumSum, 0) + 1

        return res
        