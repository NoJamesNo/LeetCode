#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        poop = []
        for i in nums:
            result[i] = result.get(i,0) + 1 
        x = sorted(result.items(), key=lambda item: item[1], reverse = True)
        print(x)
        i = 0
        
        while (i < k):
            poop.append(x[i][0])
            i += 1
            
        return poop
        
        
        
# @lc code=end

