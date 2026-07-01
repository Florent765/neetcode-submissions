class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        longest = 1
        s = set(nums)

        for x in s:
            if (x - 1) not in s:
                temp = 1
                curr = x
                while (curr + 1) in s:
                    temp+=1
                    curr+=1
                longest = max(longest, temp)

        return longest