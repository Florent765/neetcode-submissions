class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def dfs(openP, closedP):
            if openP == closedP == n:
                res.append("".join(s))
                return
            
            if openP < n:
                s.append('(')
                dfs(openP + 1, closedP)
                s.pop()
            if closedP < openP:
                s.append(')')
                dfs(openP, closedP + 1)
                s.pop()
        
        dfs(0, 0)

        return res