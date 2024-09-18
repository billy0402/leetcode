#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        if all(n == 0 for n in nums):
            return "0"

        num_strings = [str(n) for n in nums]
        num_strings.sort(key=lambda x: str(x) * 10, reverse=True)
        return "".join(num_strings)


# @lc code=end
