from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []

        while k > 0:
            maxF = max(freq, key=freq.get)
            res.append(maxF)
            del freq[maxF]
            k -= 1
        
        return res