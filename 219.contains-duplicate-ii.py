#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_table = {}
        for i, n in enumerate(nums):
            if n in hash_table and i - hash_table[n] <= k:
                return True
            hash_table[n] = i

        return False


# @lc code=end
