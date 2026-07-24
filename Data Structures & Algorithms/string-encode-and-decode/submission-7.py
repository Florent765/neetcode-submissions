class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + '#' + st
        
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1
            i += 1
            length = int(length) if length != '' else 0
            word = ""
            for j in range(length):
                word += s[i+j]
            strs.append(word)
            i += length
        
        return strs
            