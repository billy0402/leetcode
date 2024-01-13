#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alphabet_counter = defaultdict(int)
        for char in s:
            alphabet_counter[char] += 1

        for char in t:
            alphabet_counter[char] -= 1

        counter = 0
        for count in alphabet_counter.values():
            counter += abs(count)

        return counter // 2


# @lc code=end
