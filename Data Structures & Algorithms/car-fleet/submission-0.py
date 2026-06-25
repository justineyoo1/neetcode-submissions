class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        consol = list(zip(position, speed))
        consol.sort(reverse = True)
        stack = []

        for pos, speed in consol:
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
                






                