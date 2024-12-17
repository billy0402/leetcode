#
# @lc app=leetcode id=2182 lang=python3
#
# [2182] Construct String With Repeat Limit
#

# @lc code=start
import heapq
from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeat_limit: int) -> str:
        results: list[str] = []

        counter = Counter(s)
        max_heap = [(-ord(c), cnt) for c, cnt in counter.items()]
        heapq.heapify(max_heap)

        while max_heap:
            char_neg, count = heapq.heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeat_limit)
            results.append(char * use)
            count -= use

            if count <= 0 or not max_heap:
                continue

            next_char_neg, next_count = heapq.heappop(max_heap)
            results.append(chr(-next_char_neg))
            next_count -= 1

            if next_count > 0:
                heapq.heappush(max_heap, (next_char_neg, next_count))
            heapq.heappush(max_heap, (char_neg, count))

        return "".join(results)


# @lc code=end
