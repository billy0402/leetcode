#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#

# @lc code=start
class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        free_days = 0
        prev_end = 0

        for start, end in meetings:
            free_days += max(start - (prev_end + 1), 0)
            prev_end = max(prev_end, end)

        free_days += days - prev_end

        return free_days


# @lc code=end
