#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#


# @lc code=start
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        hash_table: dict[int, int] = {}
        for n in arr:
            hash_table[n] = hash_table.get(n, 0) + 1

        frequencies = sorted(hash_table.values())
        all_nums = len(frequencies)
        removed_nums = 0
        for i in range(all_nums):
            removed_nums += frequencies[i]
            if removed_nums > k:
                return all_nums - i

        return 0


# @lc code=end
