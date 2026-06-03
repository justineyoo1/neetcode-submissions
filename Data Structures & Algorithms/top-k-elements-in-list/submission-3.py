class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #step 1: counter

        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1

        #step 2: bucket sort

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqMap.items():
            bucket[freq].append(num)

        #step 3: get results
        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res






        
        
        