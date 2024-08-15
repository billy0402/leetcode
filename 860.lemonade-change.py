#
# @lc app=leetcode id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            else:  # bill == 20  # noqa: PLR5501
                if ten > 0:
                    five -= 1
                    ten -= 1
                else:
                    five -= 3

            if five < 0 or ten < 0:
                return False

        return True


# @lc code=end
