#
# @lc app=leetcode id=3541 lang=python3
#
# [3541] Find Most Frequent Vowel and Consonant
#

# @lc code=start
from collections import defaultdict

VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter: dict[str, int] = defaultdict(int)
        max_vowels = 0
        max_consonants = 0

        for c in s:
            if c in VOWELS:
                counter[c] += 1
                max_vowels = max(max_vowels, counter[c])
            else:
                counter[c] += 1
                max_consonants = max(max_consonants, counter[c])

        return max_vowels + max_consonants


# @lc code=end
