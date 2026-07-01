class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        t = []
        for num, cpt in count.items():
            t.append([cpt, num])
        t.sort()

        res = []

        while len(res) < k:
            res.append(t.pop()[1])
        return res