from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cpt = Counter(nums)
        res = []

        for i in range(k):
            curr = max(cpt, key=cpt.get)
            res.append(curr)
            del cpt[curr]
        
        return res