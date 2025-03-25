#
# @lc app=leetcode id=3394 lang=python3
#
# [3394] Check if Grid can be Cut into Sections
#

# @lc code=start
MAX_SECTIONS = 3


class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]  # (start_x, end_x)
        y = [(r[1], r[3]) for r in rectangles]  # (start_y, end_y)

        x.sort()
        y.sort()

        return (
            max(self.count_non_overlapping(x), self.count_non_overlapping(y))
            >= MAX_SECTIONS
        )

    def count_non_overlapping(self, intervals: list[tuple[int, int]]) -> int:
        count = 0
        prev_end = -1
        for start, end in intervals:
            if start >= prev_end:
                count += 1
            prev_end = max(prev_end, end)
        return count


# @lc code=end
