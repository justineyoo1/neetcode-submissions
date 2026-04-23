class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #so return a list of how many indexes until a greater value is reached
        #EX: Input: [1, 0 ,3]
        #EX: Output: [2, 1, 0]

     

        #have a tuple of all values in list with the orignal index: (38, 1)

        #stack
        #also subtract indexes of the higher value vs current


        #edge case for empty
        if not temperatures:
            return []

            #initialize with first value

        stack = [(temperatures[0], 0)]

        #[0, 0, 0, 0, 0, 0]

        res = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            #stack: [(30, 0)]
            while stack and val > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((val, i)) 

        return res





        