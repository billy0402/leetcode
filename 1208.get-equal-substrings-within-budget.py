#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        max_length = 0
        current_cost = 0
        left = 0

        for right in range(len(s)):
            current_cost += abs(ord(s[right]) - ord(t[right]))

            while current_cost > max_cost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


# @lc code=end
