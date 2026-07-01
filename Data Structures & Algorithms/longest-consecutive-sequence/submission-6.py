class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        c = collections.Counter(nums)

        for num in nums:
            curr = 1
            if num - 1 not in c:
                while num + 1 in c:
                    curr += 1
                    num = num + 1
                
                longest = max(longest, curr)
            else:
                continue
        
        return longest