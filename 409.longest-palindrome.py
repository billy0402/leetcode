#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest_length = 0
        seen: set[str] = set()

        for char in s:
            if char in seen:
                longest_length += 2
                seen.remove(char)
            else:
                seen.add(char)

        if seen:
            longest_length += 1

        return longest_length


# @lc code=end
