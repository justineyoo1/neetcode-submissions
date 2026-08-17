class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #freqMap of every word in nums
        freqMap = Counter(nums)
        heap = []

        for freq, num in freqMap.items():
            heapq.heappush(heap, (num, freq))
            
            if len(heap) > k:
                heapq.heappop(heap)
            
        
        return [v[1] for v in heap]


        


        
        