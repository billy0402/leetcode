#
# @lc app=leetcode id=2825 lang=python3
#
# [2825] Make String a Subsequence Using Cyclic Increments
#

# @lc code=start
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j = 0
        for c1 in str1:
            if j == len(str2):
                break

            c2 = str2[j]
            if c1 == c2 or ord(c1) + 1 == ord(c2) or ord(c1) - 25 == ord(c2):
                j += 1
        return j == len(str2)


# @lc code=end
