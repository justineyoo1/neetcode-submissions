class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        L = 0
        R = rows * cols - 1

        while L <= R:
            mid = (L + R) // 2
            r = mid // cols 
            c = mid % cols
            val = matrix[r][c]
            if val == target:
                return True
            elif val < target:
                L = mid + 1
            else:
                R = mid - 1

        return False




        