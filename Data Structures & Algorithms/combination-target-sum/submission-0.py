class Solution:
    def backtrack(self, nums, target, sum, i, curr, res):
            if sum == target:
                res.append(curr.copy())
                return
            elif sum > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            self.backtrack(nums, target, sum + nums[i], i, curr, res)
            curr.pop()
            self.backtrack(nums, target, sum, i + 1, curr, res)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        self.backtrack(nums, target, 0, 0, curr, res)

        return res