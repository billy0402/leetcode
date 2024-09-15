#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#

# @lc code=start
VOWELS = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        max_length = 0
        mask = 0
        first_occurrence = {0: -1}

        for i, char in enumerate(s):
            if char in VOWELS:
                mask ^= VOWELS[char]

            if mask in first_occurrence:
                max_length = max(i - first_occurrence[mask], max_length)
            else:
                first_occurrence[mask] = i

        return max_length


# @lc code=end
