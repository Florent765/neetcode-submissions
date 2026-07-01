class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {}
        for str in strs:
            _s = tuple(sorted(str))
            t.setdefault(_s, []).append(str)
        return list(t.values())