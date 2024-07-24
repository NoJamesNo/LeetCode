#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        result = []
        for i in range(len(nums)):
            #key equals index
            dic[nums[i]]= i
            #if same number already exists as key, will be replaced as
            # latter, but doesnt matter as we get previous index
            # when iterating list again
            
        for i in range(len(nums)):
            if (target - nums[i]) in dic and (i != dic[target-nums[i]]):
                result.append(i)
                result.append(dic[target-nums[i]])
                return result
                 
# @lc code=end

