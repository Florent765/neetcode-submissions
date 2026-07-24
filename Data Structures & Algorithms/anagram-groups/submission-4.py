class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = collections.defaultdict(list)

        for s in strs:
            if tuple(sorted(s)) in seen:
                seen[tuple(sorted(s))].append(s)
            else:
                seen[tuple(sorted(s))].append(s)
        return list(seen.values())
