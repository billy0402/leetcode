#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
import bisect


class MyCalendar:
    def __init__(self):
        self.calendar: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.calendar, (start, end))

        if (index - 1 >= 0 and start < self.calendar[index - 1][1]) or (
            index < len(self.calendar) and end > self.calendar[index][0]
        ):
            return False

        bisect.insort_left(self.calendar, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# print(obj.book(10, 20))
# print(obj.book(15, 25))
# print(obj.book(20, 30))
# @lc code=end
