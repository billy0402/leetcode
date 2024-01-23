#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        half = len(nums) // 2
        hash_table = {}

        for n in nums:
            hash_table[n] = hash_table.get(n, 0) + 1

            if hash_table[n] > half:
                return n

        return -1


# @lc code=end
