class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] += 1
        

        #use the values from freqmap to know where to put the indexes for nums
        #ex: if fremap was 0: 2, 1: 3, 2: 4,
        #we know that from idx 0-2 will be 0, idx 3-6 will be 1, etc
        #[0:1, 1:2, 2:1]

        r_idx = 0

        for idx in range(freqMap[0]):
            nums[r_idx] = 0
            r_idx += 1

        for idx in range(freqMap[1]):
            nums[r_idx] = 1
            r_idx += 1

        for idx in range(freqMap[2]):
            nums[r_idx] = 2
            r_idx += 1

        #be careful with using idx in multiple places (local/ global beware)

        return nums
        