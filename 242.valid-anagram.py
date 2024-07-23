#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        
        for i in s:
            dic[i] = dic.get(i, 0 ) + 1
        for i in t:
            if dic.get(i):
                dic[i] -= 1
                if dic[i] == -1:
                    return False
            else:
                return False
        return True
# @lc code=end

