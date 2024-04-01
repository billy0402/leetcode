#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if counter > 0:
                    break
            else:
                counter += 1

        return counter


# @lc code=end
