#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
import heapq

MAX_SUB_LENGTH = 2


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        queue: list[tuple[int, str]] = []
        if a > 0:
            heapq.heappush(queue, (-a, "a"))
        if b > 0:
            heapq.heappush(queue, (-b, "b"))
        if c > 0:
            heapq.heappush(queue, (-c, "c"))

        results: list[str] = []
        while queue:
            count, char = heapq.heappop(queue)
            count = -count
            if (
                len(results) >= MAX_SUB_LENGTH
                and results[-1] == char
                and results[-2] == char
            ):
                if not queue:
                    break
                current_count, current_char = heapq.heappop(queue)
                current_count = -current_count
                results.append(current_char)
                current_count -= 1
                if current_count > 0:
                    heapq.heappush(queue, (-current_count, current_char))
                heapq.heappush(queue, (-count, char))
            else:
                results.append(char)
                count -= 1
                if count > 0:
                    heapq.heappush(queue, (-count, char))
        return "".join(results)


# @lc code=end
