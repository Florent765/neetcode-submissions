class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(i, j):
            if (i < 0 or
                j < 0 or
                i >= ROWS or
                j >= COLS or
                grid[i][j] == '0'):
                return

            grid[i][j] = '0'
            for dx, dy in dirs:
                dfs(i + dx, j + dy)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    dfs(row, col)
                    islands += 1
    
        return islands