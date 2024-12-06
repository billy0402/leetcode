#
# @lc app=leetcode id=2554 lang=python3
#
# [2554] Maximum Number of Integers to Choose From a Range I
#

# @lc code=start
class Solution:
    def maxCount(self, banned: list[int], n: int, max_sum: int) -> int:
        black_list = set(banned)
        count = 0

        for i in range(1, n + 1):
            if i in black_list:
                continue

            if max_sum - i < 0:
                return count

            max_sum -= i
            count += 1

        return count


# @lc code=end
