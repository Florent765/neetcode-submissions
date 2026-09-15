class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        d = defaultdict(list)

        for s in strs:
            anagram = tuple(sorted(s))
            d[anagram].append(s)
        
        return list(d.values())