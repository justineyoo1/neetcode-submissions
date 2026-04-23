class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Example Input:
        #nums =[1,2,2,3,3,3], k = 2

        #first count up (freqMap)
        #bucket sort (idx: is count, value: num that has that count)
        #get the values in reverse order and append into res until len(res) = k


        freqMap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)

        for n, c in freqMap.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        
        
        