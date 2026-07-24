class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        box = defaultdict(set)

        for i in range(ROWS):
            row = set()
            col = set()
            for j in range(COLS):
                box_id = (i // 3, j // 3)
                if (board[i][j] != '.' and board[i][j] in row or 
                    board[j][i] != '.' and board[j][i] in col or
                    board[i][j] != '.' and board[i][j] in box[box_id]):
                    return False
                row.add(board[i][j])
                col.add(board[j][i])
                box[box_id].add(board[i][j])
        
        return True