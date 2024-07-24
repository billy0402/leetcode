#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#

# @lc code=start
class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        mapped: list[tuple[int, int]] = []

        for i, n in enumerate(nums):
            mapped_n = 0
            for char in str(n):
                mapped_n *= 10
                mapped_n += mapping[int(char)]

            mapped.append((mapped_n, i))

        mapped.sort()

        return [nums[i] for _, i in mapped]


# @lc code=end
