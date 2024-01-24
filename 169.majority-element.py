#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
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
