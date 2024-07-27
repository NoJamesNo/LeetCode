#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for strin in strs:
            count = [0] * 26 #0 = a 
            for c in strin:
                count[(ord(c) - ord('a'))] += 1
                
            result[tuple(count)] = result.get(tuple(count),[]) + [strin]

        return result.values()
# @lc code=end

