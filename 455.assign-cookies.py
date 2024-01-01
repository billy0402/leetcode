#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        counter = 0
        for i in range(len(g)):
            greed = g[i]

            for j in range(len(s)):
                size = s[j]
                if size < greed:
                    continue

                counter += 1
                s = s[:j] + s[j + 1:]
                break

        return counter


# @lc code=end
