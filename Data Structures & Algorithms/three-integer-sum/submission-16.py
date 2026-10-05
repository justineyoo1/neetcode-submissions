class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #The output should not contain any duplicate triplets

        sortedNums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            L = i + 1
            R = len(nums) - 1

            while L < R:
                total = sortedNums[i] + sortedNums[L] + sortedNums[R]
                #[-4, -1, -1, 0, 1, 2]

                if total == 0:
                    res.append([sortedNums[i], sortedNums[L], sortedNums[R]])
                    L += 1
                    R -= 1
                    while L < R and sortedNums[L] == sortedNums[L - 1]:
                        L += 1
                    while L < R and sortedNums[R] == sortedNums[R + 1]:
                        R -= 1
                elif total < 0:
                    L += 1
                else:
                    R -= 1
        return res
                
                
                
