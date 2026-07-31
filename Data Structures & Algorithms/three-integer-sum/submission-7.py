class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums) - 1
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                    continue
            L = i + 1
            R = n

            while L < R:

            
                val = nums[i] + nums[L] + nums[R]
                
                if val == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                elif val < 0:
                    L += 1
                else:
                    R -=1
        return res


        