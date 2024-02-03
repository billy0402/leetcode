#
# @lc app=leetcode id=1043 lang=python3
#
# [1043] Partition Array for Maximum Sum
#


# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n

        for i in range(n):
            largest = -1
            total = -1
            for j in range(0, min(k, i + 1)):
                largest = max(largest, arr[i - j])
                total = max(total, largest * (j + 1) + dp[i - j - 1])
            dp[i] = total

        return dp[-1]


# @lc code=end
