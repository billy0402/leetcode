#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#


# @lc code=start
class Solution:
    def twoOutOfThree(
        self,
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
    ) -> list[int]:
        hash_table: dict[int, int] = {}
        for n in set(nums1):
            hash_table[n] = hash_table.get(n, 0) + 1
        for n in set(nums2):
            hash_table[n] = hash_table.get(n, 0) + 1
        for n in set(nums3):
            hash_table[n] = hash_table.get(n, 0) + 1
        return [key for key, value in hash_table.items() if value >= 2]


# @lc code=end
