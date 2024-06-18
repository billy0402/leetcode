#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc code=start
class Solution:
    def maxProfitAssignment(
        self,
        difficulty: list[int],
        profit: list[int],
        worker: list[int],
    ) -> int:
        job_profit = list(zip(difficulty, profit, strict=False))
        job_profit.sort()

        worker.sort()

        total_profit, max_profit, index = 0, 0, 0
        n = len(worker)
        for ability in worker:
            while index < n and ability >= job_profit[index][0]:
                max_profit = max(max_profit, job_profit[index][1])
                index += 1
            total_profit += max_profit
        return total_profit


# @lc code=end
