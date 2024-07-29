#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start
class Solution:
    def numTeams(self, rating: list[int]) -> int:
        teams = 0
        n = len(rating)

        for i in range(n):
            left_bigger = 0
            left_smaller = 0
            for j in range(0, i):
                if rating[j] > rating[i]:
                    left_bigger += 1
                elif rating[j] < rating[i]:
                    left_smaller += 1

            right_bigger = 0
            right_smaller = 0
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    right_bigger += 1
                elif rating[j] < rating[i]:
                    right_smaller += 1

            teams += left_bigger * right_smaller + left_smaller * right_bigger

        return teams


# @lc code=end
