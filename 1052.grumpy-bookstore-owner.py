#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(
        self,
        customers: list[int],
        grumpy: list[int],
        minutes: int,
    ) -> int:
        n = len(customers)
        base_satisfied = sum(
            c * (1 - g) for c, g in zip(customers, grumpy, strict=True)
        )
        extra_satisfied = sum(
            c * g for c, g in zip(customers[:minutes], grumpy[:minutes], strict=True)
        )
        max_extra_satisfied = extra_satisfied

        for i in range(minutes, n):
            extra_satisfied += customers[i] * grumpy[i]
            extra_satisfied -= customers[i - minutes] * grumpy[i - minutes]

            max_extra_satisfied = max(max_extra_satisfied, extra_satisfied)

        return base_satisfied + max_extra_satisfied


# @lc code=end
