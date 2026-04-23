class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first count up freq of each num
        #then bucket sort (where index is actually the amount of freq, 
        #and the value would be the n that shows up that much
        #then add to results until the length of result equals K

        freqMap = {}
        #list of lists for the amount of values in num
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        #[1 : 1, 2 : 2, 3 : 3]

        for n, c in freqMap.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        
        



        

        
        
        