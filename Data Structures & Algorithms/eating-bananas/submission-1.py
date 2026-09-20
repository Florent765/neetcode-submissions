class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2
            
            time = h
            for pile in piles:
                time -= -(pile // -m)
            
            if time < 0:
                l = m + 1
            else:
                r = m - 1
        
        return l