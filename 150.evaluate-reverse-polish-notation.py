#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '/' and i != '*':
                stack.append(int(i))
            if i == '+':
                result = stack[-1]
                stack.pop()
                stack[-1] = stack[-1] + result
            if i == '*':
                result = stack[-1]
                stack.pop()
                stack[-1] = stack[-1] * result
            if i == '-':
                result = stack[-1]
                stack.pop()
                stack[-1] = stack[-1] - result
            if i == '/':
                result = stack[-1]
                stack.pop()
                stack[-1] = int(stack[-1] / result)
        return stack[0]        
                
                
                
# @lc code=end

