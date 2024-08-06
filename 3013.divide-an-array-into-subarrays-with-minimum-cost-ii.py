#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
import heapq


class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = [0] * 26
        for char in word:
            counter[ord(char) - ord("a")] -= 1
        heapq.heapify(counter)

        total_pushes = 0
        i = 0
        while counter:
            freq = heapq.heappop(counter)
            if freq == 0:
                break
            total_pushes += (i // 8 + 1) * -(freq)
            i += 1
        return total_pushes


# @lc code=end
