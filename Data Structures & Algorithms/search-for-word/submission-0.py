class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True

            if (row < 0 or col < 0 or 
                row >= r or col >= c or 
                board[row][col] != word[i] or 
                (row, col) in path):
                return False
            
            path.add((row, col))
            res = (dfs(row+1, col, i+1) or
                   dfs(row-1, col, i+1) or
                   dfs(row, col+1, i+1) or
                   dfs(row, col-1, i+1))
            path.remove((row, col))
            return res

        for k in range(r):
            for l in range(c):
                if dfs(k, l, 0):
                    return True
        return False