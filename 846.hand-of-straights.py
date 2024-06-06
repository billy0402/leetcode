#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], group_size: int) -> bool:
        if len(hand) % group_size != 0:
            return False

        counter = Counter(hand)

        while counter:
            min_n = min(counter)

            for i in range(group_size):
                n = min_n + i
                if n not in counter:
                    return False

                counter[n] -= 1
                if counter[n] == 0:
                    del counter[n]

        return True


# @lc code=end
