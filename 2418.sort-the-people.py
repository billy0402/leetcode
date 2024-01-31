#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#


# @lc code=start
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        peoples = sorted(zip(names, heights), key=lambda x: -x[1])
        return [name for name, _ in peoples]


# @lc code=end
