class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row check

        for rows in board:
            seen = set()
            for val in rows:
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for board_row in range(0, 9, 3):
            for board_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[board_row + i][board_col +j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True



        