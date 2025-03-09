#
# @lc app=leetcode id=3208 lang=python3
#
# [3208] Alternating Groups II
#

# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        counter, l, n = 0, 0, len(colors)

        for r in range(1, n + k - 1):
            # sliding window is not alternating
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
            # keep sliding window size
            if r - l + 1 > k:
                l += 1
            # sliding window is alternating
            if r - l + 1 == k:
                counter += 1

        return counter


# @lc code=end
