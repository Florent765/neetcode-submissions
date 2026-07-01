class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        c = collections.Counter(nums)

        for num in nums:
            curr = 1

            while num + 1 in c:
                curr += 1
                num = num + 1
            
            longest = max(longest, curr)
        
        return longest