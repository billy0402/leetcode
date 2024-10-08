#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        left_brackets = 0

        for char in s:
            if char == "[":
                left_brackets += 1
            elif left_brackets:
                left_brackets -= 1

        return (left_brackets + 1) // 2


# @lc code=end
