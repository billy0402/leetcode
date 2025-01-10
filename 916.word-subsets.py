#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
from collections import Counter


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        results: list[str] = []

        counter2: Counter[str] = Counter()
        for word in words2:
            counter2 |= Counter(word)

        for word in words1:
            counter1 = Counter(word)

            if all(count <= counter1.get(char, 0) for char, count in counter2.items()):
                results.append(word)

        return results


# @lc code=end
