#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack:
                if
            stack.append([t,i])        
# @lc code=end
