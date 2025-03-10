#
# @lc app=leetcode id=3305 lang=python3
#
# [3305] Count of Substrings Containing Every Vowel and K Consonants I
#

# @lc code=start
VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        counter, n = 0, len(word)

        for i in range(n - (k + 5) + 1):
            vowels: set[str] = set()
            consonants = 0

            while i < n:
                char = word[i]
                if char in VOWELS:
                    vowels.add(word[i])
                else:
                    consonants += 1

                if len(vowels) == len(VOWELS) and consonants == k:
                    counter += 1
                elif consonants > k:
                    break

                i += 1  # noqa: PLW2901

        return counter


# @lc code=end
