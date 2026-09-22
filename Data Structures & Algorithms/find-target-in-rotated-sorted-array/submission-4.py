class Solution:
    def binary_search(self, nums, target, l, r):
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        if target <= nums[-1]:
            return self.binary_search(nums, target, l, len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, l - 1)
