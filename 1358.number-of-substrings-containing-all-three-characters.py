#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter, l, n = 0, 0, len(s)
        freq: dict[str, int] = defaultdict(int)

        for r in range(n):
            freq[s[r]] += 1

            while len(freq) == 3:  # noqa: PLR2004
                counter += n - r

                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

        return counter


# @lc code=end
