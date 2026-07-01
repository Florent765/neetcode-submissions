class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for st in strs:
            s += str(len(st)) + '#' + st
        
        return s
    
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            length = ''
            while s[j] != '#':
                length += s[j]
                j += 1
            
            length = int(length)
            word = s[j + 1: j + 1 + length]
            strs.append(word)
            i = j + 1 + length
        
        return strs