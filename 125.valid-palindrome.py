#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalpha() and not s[left].isnumeric():
                left += 1
            elif not s[right].isalpha() and not s[right].isnumeric():
                right -= 1
            elif s[right].lower() != s[left].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
        
# @lc code=end
butt = Solution()
butt.isPalindrome("0P")

