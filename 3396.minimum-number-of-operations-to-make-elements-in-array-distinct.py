#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen: set[int] = set()

        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if n in seen:
                return i // 3 + 1  # remove 3 elements at least once
            seen.add(n)

        return 0


# @lc code=end
