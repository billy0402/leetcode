#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#


# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        answers: list[int] = []
        digits = '123456789'

        for i in range(len(digits)):
            for j in range(i + 1, len(digits) + 1):
                num = int(digits[i:j])
                if low <= num <= high:
                    answers.append(num)

        answers.sort()
        return answers


# @lc code=end
