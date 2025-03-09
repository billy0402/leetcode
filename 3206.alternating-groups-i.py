#
# @lc app=leetcode id=3206 lang=python3
#
# [3206] Alternating Groups I
#

# @lc code=start
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        counter, n = 0, len(colors)

        for i in range(len(colors)):
            j = (i + 1) % n
            k = (i + 2) % n
            if colors[i] != colors[j] and colors[j] != colors[k]:
                counter += 1

        return counter


# @lc code=end
