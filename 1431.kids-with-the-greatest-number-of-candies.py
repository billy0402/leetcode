#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#


# @lc code=start
class Solution:
    def kidsWithCandies(
        self,
        candies: list[int],
        extraCandies: int,
    ) -> list[bool]:
        results: list[bool] = []
        largest = max(candies)

        for childCandies in candies:
            totalCandies = childCandies + extraCandies
            results.append(totalCandies >= largest)

        return results


# @lc code=end
