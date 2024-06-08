#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
MIN_LENGTH = 2


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_mod = 0
        # { remainder: index }
        # Default { 0, -1 } to make prefix_mod valid with mod 0.
        mod_seen = {0: -1}

        for i, n in enumerate(nums):
            prefix_mod = (prefix_mod + n) % k

            """
            If prefix_mod has been seen,
            it means there is a valid subarray within this range.
            (23) % 6 = 5
            (23 + 2) % 6 = 1
            (23 + 2 + 4) % 6 = 5
            [2, 4] is the valid subarray.
            """
            if prefix_mod not in mod_seen:
                mod_seen[prefix_mod] = i
            elif i - mod_seen[prefix_mod] >= MIN_LENGTH:
                return True

        return False


# @lc code=end
