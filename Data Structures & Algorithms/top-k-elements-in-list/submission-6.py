class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        
        #Count
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        #Bucket Sort
        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        for val, freq in freqMap.items():
            bucket[freq].append(val)

        #reverse
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res            
        