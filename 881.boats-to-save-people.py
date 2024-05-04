#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#


# @lc code=start
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1

        return boats


# @lc code=end
