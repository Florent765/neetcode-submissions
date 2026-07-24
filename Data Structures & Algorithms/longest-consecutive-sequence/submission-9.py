class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        s = set(nums)
        i = 0

        while i < len(nums):
            if nums[i] - 1 not in s:
                curr = 1
                while nums[i] + 1 in s:
                    curr += 1
                    nums[i] += 1

                maxL = max(maxL, curr)
            i += 1
        
        return maxL