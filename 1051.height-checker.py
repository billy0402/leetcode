#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#


# @lc code=start
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        counter = 0
        expected = sorted(heights)
        for h, e in zip(expected, heights):
            if h != e:
                counter += 1
        return counter


# @lc code=end
