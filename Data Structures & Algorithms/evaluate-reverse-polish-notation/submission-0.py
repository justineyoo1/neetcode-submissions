class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        
        for val in tokens:
            if val in operations:
                if val == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                elif val == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif val == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(val))

        return stack[0]

        