#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#

# @lc code=start
class MyCalendarTwo:
    def __init__(self):
        self.non_overlapping: list[tuple[int, int]] = []
        self.overlapping: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if end > s and e > start:
                return False

        for s, e in self.non_overlapping:
            if end > s and e > start:
                self.overlapping.append(
                    (max(s, start), min(e, end)),
                )
        self.non_overlapping.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# print(obj.book(10, 20))
# print(obj.book(50, 60))
# print(obj.book(10, 40))
# print(obj.book(5, 15))
# print(obj.book(5, 10))
# print(obj.book(25, 55))
# @lc code=end
