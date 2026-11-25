class Solution:
    def eat(self, piles, k):
        return sum((pile + k - 1) // k for pile in piles)

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2

            if self.eat(piles, m) > h:
                l = m + 1
            else:
                r = m - 1
        
        return l