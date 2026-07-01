from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cpt = Counter(nums)
        res = []

        while k > 0:
            res.append(max(cpt, key=cpt.get))
            cpt.pop(max(cpt, key=cpt.get))
            k-=1
        
        return res