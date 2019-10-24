import sys

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minVal = sys.maxsize

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.compareMin(x)
        

    def pop(self) -> None:
        if len(self.stack) != 0:
            top = self.stack.pop()
            self.comparePop(top)
            

    def top(self) -> int:
        if len(self.stack) != 0:
            top = self.stack[-1]
            return top
        else:
            return -1

    def getMin(self) -> int:
        if len(self.stack) != 0:
            return self.minVal
        else:
            return -1
        
        
    def compareMin(self, x):
        if x < self.minVal:
            self.minVal = x
        
    def comparePop(self, x):
        if x == self.minVal:
            if len(self.stack) != 0:
                self.minVal = min(self.stack)
            else:
                self.minVal = sys.maxsize
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()