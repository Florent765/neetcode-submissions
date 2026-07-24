class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []

        while k > 0:
            maxC = max(c, key=c.get)
            res.append(maxC)
            del c[maxC]
            k -= 1
            
        return res