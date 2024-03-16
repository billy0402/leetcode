#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#


# @lc code=start
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        # { count: first_seen_at }
        seen_at = {0: -1}
        max_length = count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1

            if count in seen_at:
                max_length = max(max_length, i - seen_at[count])
            else:
                seen_at[count] = i

        return max_length


# @lc code=end
