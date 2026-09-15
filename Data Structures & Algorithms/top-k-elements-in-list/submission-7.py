class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        while k > 0:
            maxF = max(count, key=count.get)
            res.append(maxF)
            k -= 1
            del count[maxF]
        
        return res