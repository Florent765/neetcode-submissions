class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(k):
            if k >= len(nums):
                return 0
            if cache[k] != -1:
                return cache[k]
            cache[k] = max(nums[k] + dfs(k + 2), dfs(k + 1))
            return cache[k]

        return dfs(0)