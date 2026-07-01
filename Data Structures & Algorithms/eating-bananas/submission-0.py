class Solution:
    def hours(self, piles: List[int], k: int) -> int:
        res = 0
        for pile in piles:
            res += (pile + k - 1) // k
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2

            if self.hours(piles, m) > h:
                l = m + 1
            else:
                r = m - 1
        
        return l