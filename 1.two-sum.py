#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, n in enumerate(nums):
            remain = target - n
            if remain in hash_table:
                return [hash_table[remain], i]

            hash_table[n] = i

        return []


# @lc code=end
