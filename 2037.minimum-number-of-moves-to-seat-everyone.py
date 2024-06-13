#
# @lc app=leetcode id=2037 lang=python3
#
# [2037] Minimum Number of Moves to Seat Everyone
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0

        for seat, student in zip(seats, students, strict=False):
            moves += abs(student - seat)

        return moves


# @lc code=end
