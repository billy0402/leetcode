#
# @lc app=leetcode id=1508 lang=python3
#
# [1508] Range Sum of Sorted Subarray Sums
#

# @lc code=start
MOD = 10**9 + 7


class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sums: list[int] = []

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                sums.append(total)

        sums.sort()

        return sum(sums[left - 1 : right]) % MOD


# @lc code=end
