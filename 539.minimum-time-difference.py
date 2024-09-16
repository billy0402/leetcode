#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
MAX_MINUTES = 24 * 60


class Solution:
    def findMinDifference(self, time_points: list[str]) -> int:
        minutes = sorted([int(time[:2]) * 60 + int(time[3:]) for time in time_points])
        minutes.append(MAX_MINUTES + minutes[0])
        return min(minutes[i] - minutes[i - 1] for i in range(1, len(minutes)))


# @lc code=end
