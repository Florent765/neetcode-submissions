class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for str in strs:
            enc = enc + str + "¡"
        return enc

    def decode(self, s: str) -> List[str]:
        t = []
        i = 0
        while i < len(s):
            temp = ""
            cpt = i
            while s[cpt] != "¡" and cpt < len(s):
                temp = temp + s[cpt]
                cpt+=1
            i = cpt
            t.append(temp)
            i+=1
        return t