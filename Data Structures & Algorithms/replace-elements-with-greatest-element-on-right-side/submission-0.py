class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxLargest = -1


        for i in range(len(arr) -1 , -1, -1):

            temp = arr[i]

            arr[i] = maxLargest

            if temp > maxLargest:
                maxLargest = temp
            

        
        return arr