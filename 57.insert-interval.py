#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def insert(
        self,
        intervals: list[list[int]],
        new_interval: list[int],
    ) -> list[list[int]]:
        n = len(intervals)
        i = 0
        answer: list[list[int]] = []
        new_start, new_end = new_interval

        while i < n and intervals[i][1] < new_start:
            answer.append(intervals[i])
            i += 1

        while i < n and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        answer.append([new_start, new_end])

        while i < n:
            answer.append(intervals[i])
            i += 1

        return answer


# @lc code=end
