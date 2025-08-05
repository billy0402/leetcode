#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#

# @lc code=start
class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        count = 0

        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets[i] = -1
                    break
            else:
                count += 1

        return count


# @lc code=end
