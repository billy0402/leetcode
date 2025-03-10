#
# @lc app=leetcode id=3306 lang=python3
#
# [3306] Count of Substrings Containing Every Vowel and K Consonants II
#

# @lc code=start
from collections import defaultdict

VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        return self._at_least_k(word, k) - self._at_least_k(word, k + 1)

    def _at_least_k(self, word: str, k: int) -> int:
        counter = 0
        vowels: dict[str, int] = defaultdict(int)
        consonants = 0
        l = 0

        for r in range(len(word)):
            if word[r] in VOWELS:
                vowels[word[r]] += 1
            else:
                consonants += 1

            while len(vowels) == len(VOWELS) and consonants >= k:
                counter += len(word) - r
                if word[l] in VOWELS:
                    vowels[word[l]] -= 1
                    if vowels[word[l]] == 0:
                        vowels.pop(word[l])
                else:
                    consonants -= 1
                l += 1

        return counter


# @lc code=end
