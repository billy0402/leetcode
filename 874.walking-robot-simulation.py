#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
# ("N", "E", "S", "W")
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
TURN_LEFT = -1
TURN_RIGHT = -2


class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        max_distance_squared = 0
        x, y, d = 0, 0, 0
        obstacle_set = {tuple(obstacle) for obstacle in obstacles}

        for command in commands:
            if command == TURN_LEFT:
                d = (d + 1) % 4
            elif command == TURN_RIGHT:
                d = (d - 1) % 4
            else:
                for _ in range(command):
                    mx, my = DIRECTIONS[d]
                    nx, ny = x + mx, y + my
                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared


# @lc code=end
