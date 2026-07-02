class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        seen = set()
        curr = 0

        def dfs():
            nonlocal curr
            if curr == target and tuple(sorted(sol)) not in seen:
                seen.add(tuple(sorted(sol)))
                res.append(sol[:])
                return
            
            for num in nums:
                if curr + num <= target:
                    sol.append(num)
                    curr += num
                    dfs()
                    sol.pop()
                    curr -= num
        
        dfs()
        return res