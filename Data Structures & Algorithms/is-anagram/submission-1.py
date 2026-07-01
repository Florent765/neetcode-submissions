class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = 0
        l2 = 0
        p1 = 1
        p2 = 1
        for i in s:
            l1 += ord(i)
            p1 *= ord(i)
        for i in t:
            l2 += ord(i)
            p2 *= ord(i)

        return len(s) == len(t) and l1 == l2 and p1 == p2