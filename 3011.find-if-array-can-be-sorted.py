#
# @lc app=leetcode id=3011 lang=python3
#
# [3011] Find if Array Can Be Sorted
#

# @lc code=start
class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        cur_min = cur_max = prev_max = prev_count = -1

        for n in nums:
            cur_count = n.bit_count()

            if cur_count == prev_count:
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)

            else:
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
                cur_min = cur_max = n
                prev_count = cur_count

        return prev_max < cur_min


# @lc code=end
