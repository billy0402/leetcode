#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
#

# @lc code=start

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = (int(s) for s in date.split('-'))

        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month_days[1] = 29
        else:
            month_days[1] = 28

        return sum(month_days[:month - 1]) + day


# @lc code=end
