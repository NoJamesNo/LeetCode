#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        result = [0] * 2
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                result[0] = left + 1
                result[1] = right + 1 
                return result
        
        
# @lc code=end
poop = Solution()
poop.twoSum([2,7,11,15],9)

 