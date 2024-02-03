#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#


# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        hash_table: dict[str, int] = {}
        counter = 0
        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                counter += 1
            hash_table[char1] = hash_table.get(char1, 0) + 1
            hash_table[char2] = hash_table.get(char2, 0) - 1

        if counter != 0 and counter != 2:
            return False

        for value in hash_table.values():
            if value != 0:
                return False

        return True


# @lc code=end
