class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.mini:
            self.minstack.append(val)
            self.mini = val

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.mini:
            self.minstack.pop()
            self.mini = self.minstack[-1] if self.minstack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
