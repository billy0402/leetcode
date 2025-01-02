#
# @lc app=leetcode id=2559 lang=python3
#
# [2559] Count Vowel Strings in Ranges
#

# @lc code=start
VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        prefix = [0] * (len(words) + 1)
        for i, w in enumerate(words):
            prefix[i + 1] = prefix[i]
            if w[0] in VOWELS and w[-1] in VOWELS:
                prefix[i + 1] += 1

        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):  # noqa: E741
            ans[i] = prefix[r + 1] - prefix[l]
        return ans


# @lc code=end
