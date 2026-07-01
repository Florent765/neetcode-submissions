class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preprod, sufprod = [1] * n, [1] * n

        prefix, suffix = 1, 1
        for i in range(n):
            preprod[i] = prefix
            prefix *= nums[i]

            sufprod[~i] = suffix
            suffix *= nums[~i]

        return [preprod[i] * sufprod[i] for i in range(n)]        