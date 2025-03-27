#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#

# @lc code=start
class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        major = self._majority_element(nums)

        left_count = 0
        right_count = nums.count(major)

        for i, n in enumerate(nums):
            if n == major:
                left_count += 1
                right_count -= 1

            left_length = i + 1
            right_length = len(nums) - left_length

            if left_count * 2 > left_length and right_count * 2 > right_length:
                return i

        return -1

    # leetcode 169
    def _majority_element(self, nums: list[int]) -> int:
        major = -1
        count = 0

        for n in nums:
            if n == major:
                count += 1
            elif count == 0:
                major = n
                count = 1
            else:
                count -= 1

        return major


# @lc code=end
