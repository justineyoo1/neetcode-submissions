class Solution:
    def isValid(self, s: str) -> bool:
        #stack(like a pringles can)
        #stack in python is a list
        #funcs (append and pop)

        closeOpenMap = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for char in s:
            #determine if its open / closed bracket
            if stack and char in closeOpenMap.keys() and closeOpenMap[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

        
        