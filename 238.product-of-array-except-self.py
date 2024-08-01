#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = nums.copy()

        for i in range(len(nums)):
            if i == 0:
                result[0] = 1
            else:
                result[i] = result[i - 1] * nums[i-1]
                    
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) -1:
                postfix = nums[-1]
            else:
                result[i] = result[i] * postfix
                postfix *= nums[i]
                
        return(result)
            

# @lc code=end

