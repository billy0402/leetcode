#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for char in ransom_note:
            if char not in counter or counter[char] <= 0:
                return False

            counter[char] -= 1

        return True


# @lc code=end
