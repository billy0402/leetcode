#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#

# @lc code=start
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        deck.sort()

        queue = deque()
        for i in range(len(deck)):
            queue.append(i)

        results = [0] * len(deck)
        for card in deck:
            index = queue.popleft()
            results[index] = card

            if queue:
                index = queue.popleft()
                queue.append(index)

        return results


# @lc code=end
