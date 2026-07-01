class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToopen:
                if not stack or stack[-1] != closeToopen[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return not stack