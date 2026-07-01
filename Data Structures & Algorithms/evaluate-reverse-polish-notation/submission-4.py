import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {'+': operator.add, 
              '-': operator.sub,
              '*': operator.mul,
              '/': lambda a, b: int(a / b)}

        stack = []

        for tok in tokens:
            if tok in op:
                a = stack.pop()
                b = stack.pop()
                res = op[tok](b, a)
                stack.append(res)
            else:
                stack.append(int(tok))

        return stack[-1]
            