#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
from collections import defaultdict


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        alphabet1 = defaultdict(int)
        alphabet2 = defaultdict(int)

        for char in word1:
            alphabet1[char] += 1

        for char in word2:
            alphabet2[char] += 1

        if alphabet1.keys() != alphabet2.keys():
            return False

        count1 = sorted(alphabet1.values())
        count2 = sorted(alphabet2.values())

        return count1 == count2


# @lc code=end
