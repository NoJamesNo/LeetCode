#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.minimum and self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stack.pop() 
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimum:
            return self.minimum[-1]
        else:
            return 0

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
