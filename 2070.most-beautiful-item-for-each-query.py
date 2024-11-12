#
# @lc app=leetcode id=2070 lang=python3
#
# [2070] Most Beautiful Item for Each Query
#

# @lc code=start
class Solution:
    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        items.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        answer = [0] * len(queries)
        j = 0
        current_max = 0
        for query, i in sorted_queries:
            while j < len(items) and items[j][0] <= query:
                current_max = max(current_max, items[j][1])
                j += 1
            answer[i] = current_max
        return answer


# @lc code=end
