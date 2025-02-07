#
# @lc app=leetcode id=3160 lang=python3
#
# [3160] Find the Number of Distinct Colors Among the Balls
#

# @lc code=start
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        result: list[int] = []
        balls: dict[int, int] = {}
        colors: dict[int, int] = defaultdict(int)

        for ball, color in queries:
            if ball in balls:
                prev_color = balls[ball]
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    del colors[prev_color]

            balls[ball] = color
            colors[color] += 1
            result.append(len(colors))

        return result


# @lc code=end
