class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq1 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1

        while r < len(s2):
            freq2 = [0] * 26
            for i in range(l, r + 1):
                freq2[ord(s2[i]) - ord('a')] += 1
            if freq1 == freq2:
                return True
            l += 1
            r += 1

        return False