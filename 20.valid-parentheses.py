#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i =='{':
                stack.append(i)
            elif i == ')':
                if not stack:
                    return False                               
                if stack[-1] == '(':
                    stack.pop()
                else: 
                    return False
            elif i == '}':
                if not stack:
                    return False                               
                if stack[-1] == '{':
                    stack.pop()
                else: 
                    return False
            elif i == ']':
                if not stack:
                    return False                               
                if stack[-1] == '[':
                    stack.pop()
                else: 
                    return False
        if not stack:
            return True
        else:
            return False      

# @lc code=end
poop = Solution()
poop.isValid("()")

