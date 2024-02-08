#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#


# @lc code=start
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            middle = (left + right) // 2

            result = guess(middle)
            if result == 0:
                return middle
            elif result == -1:
                right = middle - 1
            elif result == 1:
                left = middle + 1

        return -1


# @lc code=end
