#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#


# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for direction in moves:
            if direction == 'U':
                y -= 1
            elif direction == 'D':
                y += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1

        return x == 0 and y == 0


# @lc code=end
