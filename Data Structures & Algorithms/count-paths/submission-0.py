class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(i, j):
            if i > m - 1 or j > n - 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            
            path = 0
            path += dfs(i + 1, j)
            path += dfs(i, j + 1)
            memo[(i, j)] = path
            
            return path
        
        return dfs(0, 0)