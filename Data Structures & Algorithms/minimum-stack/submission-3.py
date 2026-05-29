class MinStack:

    def __init__(self):
        self.minStack = []
        self.curMin = float('inf')
        
    def push(self, val: int) -> None:
        # each element is going to have two components: val, min
        if self.curMin > val:
            self.curMin = val
        self.minStack.append((val, self.curMin))
        
    def pop(self) -> None:
        self.minStack.pop()
        if len(self.minStack) > 0:
            self.curMin = self.minStack[len(self.minStack) - 1][1]
        else:
            self.curMin = float('inf')
        
    def top(self) -> int:
        return self.minStack[len(self.minStack) - 1][0]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1][1]

        
