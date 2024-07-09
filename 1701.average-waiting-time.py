#
# @lc app=leetcode id=1701 lang=python3
#
# [1701] Average Waiting Time
#

# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current = 0
        total = 0

        for arrival, time in customers:
            current = max(current, arrival) + time
            total += current - arrival

        return total / len(customers)


# @lc code=end
