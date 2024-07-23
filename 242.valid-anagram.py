#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        first_size = 0
        for i in s:
            first_size += 1
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        for i in t:
            first_size -= 1
            if dic.get(i):
                dic[i] -= 1
                if dic[i] == -1:
                    return False
            else:
                return False
        if first_size == 0:
            return True
        return False
# @lc code=end

