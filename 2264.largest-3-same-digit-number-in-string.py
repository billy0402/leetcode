#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#


# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        same_digits = []
        for index in range(len(num) - 2):
            n1 = num[index]
            n2 = num[index + 1]
            n3 = num[index + 2]
            if n2 == n1 and n3 == n2:
                same_digits.append(n1)

        return max(same_digits) * 3 if same_digits else ''


# @lc code=end
