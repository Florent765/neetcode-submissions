class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for k in range(n):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            l, r = k + 1, len(nums) - 1
            target = -nums[k]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[k]])
                    l += 1
                    # r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res