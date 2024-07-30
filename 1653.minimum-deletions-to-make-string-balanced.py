#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_deletions = len(s)
        total_a = s.count("a")
        right_a = total_a
        left_b = 0

        for char in s:
            if char == "a":
                right_a -= 1
            min_deletions = min(min_deletions, left_b + right_a)
            if char == "b":
                left_b += 1

        return min_deletions


# @lc code=end
