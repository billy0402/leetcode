#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        def go_next(city):
            next = [next for start, next in paths if start == city]
            if not next:
                return city

            go_next(next[0])

        if len(paths) == 1:
            return paths[0][1]

        for start, next in paths:
            destination = go_next(next)
            if destination:
                break

        return destination


# @lc code=end
