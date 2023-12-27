#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        pointer = None

        for i in range(len(colors) - 1):
            if pointer and i < pointer or colors[i] != colors[i + 1]:
                continue

            for j in range(i + 1, len(colors)):
                if colors[i] != colors[j]:
                    break

                pointer = j

            repeated = neededTime[i:pointer + 1]
            m = max(repeated)
            s = sum(repeated)
            time += s - m

        return time


# @lc code=end
