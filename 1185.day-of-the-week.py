#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
#

# @lc code=start
from datetime import datetime

WEEKDAYS = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
)


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        past = datetime(year, month, day)
        weekday = past.weekday()
        return WEEKDAYS[weekday]


# @lc code=end
