#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        answer1 = set()
        answer2 = set()

        for winner, loser in matches:
            losers[loser] += 1

            answer1.add(winner)

            if losers[loser] == 1:
                answer2.add(loser)
            elif losers[loser] == 2:
                answer2.remove(loser)

        for key in losers.keys():
            if key in answer1:
                answer1.remove(key)

        return [sorted(answer1), sorted(answer2)]


# @lc code=end
