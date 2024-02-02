#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#


# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hash_table: dict[int, int] = {}

        for i, n in enumerate(sorted(nums)):
            if n not in hash_table:
                hash_table[n] = i

        return [hash_table[n] for n in nums]


# @lc code=end
