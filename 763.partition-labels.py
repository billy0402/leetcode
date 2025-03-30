#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        results: list[int] = []
        last_indexes: dict[str, int] = {char: i for i, char in enumerate(s)}
        size, end = 0, 0

        for i, char in enumerate(s):
            size += 1
            last_index = last_indexes[char]
            end = max(end, last_index)

            if i == end:
                results.append(size)
                size = 0

        return results


# @lc code=end
