#
# @lc app=leetcode id=2566 lang=python3
#
# [2566] Maximum Difference by Remapping a Digit
#

# @lc code=start
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        non_nine = 0
        while s[non_nine] == "9" and non_nine < len(s) - 1:
            non_nine += 1
        max_remap = s.replace(s[non_nine], "9")
        min_remap = s.replace(s[0], "0")
        return int(max_remap) - int(min_remap)


# @lc code=end
