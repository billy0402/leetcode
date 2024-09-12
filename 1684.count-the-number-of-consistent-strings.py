#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        counter = 0

        for word in words:
            if all(char in allowed_set for char in word):
                counter += 1

        return counter


# @lc code=end
