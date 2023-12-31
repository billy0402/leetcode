#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#


# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        n = len(s)
        first_index = {}

        for i in range(n):
            char = s[i]

            if char not in first_index:
                first_index[char] = i
                continue

            sub_length = i - first_index[char] - 1
            ans = max(ans, sub_length)
        return ans


# @lc code=end
