#
# @lc app=leetcode id=2981 lang=python3
#
# [2981] Find Longest Special Substring That Occurs Thrice I
#

# @lc code=start
from collections import defaultdict

MAX_OCCURS = 3


class Solution:
    def maximumLength(self, s: str) -> int:
        counter: dict[str, int] = defaultdict(int)
        for i in range(len(s)):
            j = i
            while j < len(s) and s[j] == s[i]:
                substring = s[i : j + 1]
                counter[substring] += 1
                j += 1

        max_length = -1
        for substring, times in counter.items():
            if times >= MAX_OCCURS:
                max_length = max(max_length, len(substring))
        return max_length


# @lc code=end
