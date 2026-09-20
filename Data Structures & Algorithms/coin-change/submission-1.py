class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(curr):
            if curr < 0:
                return float('inf')

            if curr == 0:
                return 0
            
            if curr in cache:
                return cache[curr]

            min_coins = float('inf')
            for coin in coins:
                res = dfs(curr - coin)
                min_coins = min(min_coins, res + 1)
            
            cache[curr] = min_coins
            return min_coins

        result = dfs(amount)
        return result if result != float('inf') else -1