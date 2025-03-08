#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_operations = blocks[:k].count("W")
        min_operations = current_operations

        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":  # remove left
                current_operations -= 1
            if blocks[i] == "W":  # add right
                current_operations += 1
            min_operations = min(min_operations, current_operations)

        return min_operations


# @lc code=end
