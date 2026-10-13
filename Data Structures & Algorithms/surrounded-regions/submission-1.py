class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and 
                (
                    r == 0 or
                    c == 0 or
                    r == ROWS - 1 or 
                    c == COLS - 1
                    )
                    ):
                    board[r][c] = 'M'
                    q.append((r, c))
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()

                for dx, dy in dirs:
                    row, col = r + dx, c + dy

                    if (row in range(ROWS) and
                        col in range(COLS) and
                        board[row][col] == 'O'
                        ):
                        board[row][col] = 'M'
                        q.append((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'M':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'