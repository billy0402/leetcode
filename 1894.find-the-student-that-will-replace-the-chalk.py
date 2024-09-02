#
# @lc app=leetcode id=1894 lang=python3
#
# [1894] Find the Student that Will Replace the Chalk
#

# @lc code=start
class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        k %= sum(chalk)

        for i, student_chalk in enumerate(chalk):
            k -= student_chalk

            if k < 0:
                return i

        return -1


# @lc code=end
