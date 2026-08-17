class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert to max heap by making everything negative
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)

        for _ in range(k - 1):
            heapq.heappop(maxHeap)

        return -maxHeap[0]