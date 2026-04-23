class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #no dupes in hashset thus, if n in hashset it has already appeared


        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False