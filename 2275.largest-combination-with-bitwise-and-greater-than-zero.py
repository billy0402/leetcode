#
# @lc app=leetcode id=2275 lang=python3
#
# [2275] Largest Combination With Bitwise AND Greater Than Zero
#

# @lc code=start
class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        max_count = 0

        for i in range(24):
            count = 0
            for n in candidates:
                if n & (1 << i):
                    count += 1
            max_count = max(max_count, count)

        return max_count


# @lc code=end
