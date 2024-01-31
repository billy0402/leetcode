#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#


# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        answer = [''] * len(s)
        for i, char in zip(indices, s):
            answer[i] = char
        return ''.join(answer)


# @lc code=end
