class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return nums[0]
        rob1, rob2, rob3, rob4 = 0, 0, 0, 0
        a1, a2 = nums[:n-1], nums[1:]

        for num in a1:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        
        for num in a2:
            temp = max(rob3 + num, rob4)
            rob3 = rob4
            rob4 = temp
        return max(rob2, rob4)