#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = set()
        for i in nums:
            if i in dic:
                return True
            dic.add()
        return False        
# @lc code=end
