#
# @lc app=leetcode id=3152 lang=python3
#
# [3152] Special Array II
#

# @lc code=start
class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        results: list[bool] = []
        prefix: list[int] = [0] * len(nums)

        # count the number of non-special from 0 to i
        for i in range(1, len(nums)):
            if (nums[i - 1] + nums[i]) % 2 == 0:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        for start, end in queries:
            results.append(prefix[end] - prefix[start] == 0)

        return results


# @lc code=end
