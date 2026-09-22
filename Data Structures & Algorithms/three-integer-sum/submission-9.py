class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue

            target = -nums[k]
            l, r = k + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[k]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        
        return res