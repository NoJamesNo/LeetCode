#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for i in nums:
            dic[i] = 0
        for i in nums:
            dic[i] += 1
            if dic[i] == 2:
                return True
        return False        
# @lc code=end
