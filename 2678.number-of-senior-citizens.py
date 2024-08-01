#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#

# @lc code=start
AGE_LIMIT = 60


class Solution:
    def countSeniors(self, details: list[str]) -> int:
        counter = 0

        for detail in details:
            age = int(detail[11:13])

            if age > AGE_LIMIT:
                counter += 1

        return counter


# @lc code=end
