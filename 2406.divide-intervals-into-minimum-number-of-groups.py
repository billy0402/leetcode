#
# @lc app=leetcode id=2406 lang=python3
#
# [2406] Divide Intervals Into Minimum Number of Groups
#

# @lc code=start
class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        start: list[int] = []
        end: list[int] = []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()

        result = 0
        i, j = 0, 0
        while i < len(intervals):
            if start[i] <= end[j]:
                i += 1
            else:
                j += 1
            result = max(result, i - j)
        return result


# @lc code=end
