class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        res = []

        while k > 0:
            maxK = max(c, key=c.get)
            res.append(maxK)
            del c[maxK]
            k -= 1
        
        return res