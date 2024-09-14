#
# @lc app=leetcode id=2419 lang=python3
#
# [2419] Longest Subarray With Maximum Bitwise AND
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        max_num = 0
        counter = 0
        max_length = 0

        for n in nums:
            if n > max_num:
                max_num = n
                counter = 1
                max_length = 1
            elif n == max_num:
                counter += 1
            else:
                counter = 0

            max_length = max(counter, max_length)

        return max_length


# @lc code=end
