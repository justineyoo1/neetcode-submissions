class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each string in list, get the counter version of that
        results = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            results[tuple(count)].append(string)

        return list(results.values())

        
                
        


                


        
        