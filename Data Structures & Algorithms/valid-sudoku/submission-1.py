class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #(row / 3) * 3 (col / 3) -> to find quadrant

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):

                cur = board[row][col]

                if cur == '.':
                    continue

                #row check
                if cur in rows[row]:
                    return False   
                rows[row].add(cur)

                #col check
                if cur in cols[col]:
                    return False   
                cols[col].add(cur)

                #box check
                region = (row // 3, col // 3)

                if cur in boxes[region]:
                    return False

                boxes[region].add(cur)

        return True

        