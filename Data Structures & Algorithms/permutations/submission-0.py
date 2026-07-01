class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def dfs():
            if len(perm) >= len(nums):
                res.append(perm[:])
                return
            
            for num in nums:
                if num not in perm:
                    perm.append(num)
                    dfs()
                    perm.pop()
        
        dfs()
        return res