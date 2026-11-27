class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = [False] * n
        diag1 = [False] * (2 * n)
        diag2 = [False] * (2 * n)

        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for i in range(n):
                if (col[i] or
                    diag1[i + row] or
                    diag2[i - row + n - 1]):
                    continue
                
                col[i] = True
                diag1[i + row] = True
                diag2[i - row + n - 1] = True
                board[row][i] = 'Q'

                backtrack(row + 1)

                col[i] = False
                diag1[i + row] = False
                diag2[i - row + n - 1] = False
                board[row][i] = '.'
        
        backtrack(0)
        return res