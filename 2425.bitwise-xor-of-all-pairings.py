#
# @lc app=leetcode id=2425 lang=python3
#
# [2425] Bitwise XOR of All Pairings
#

# @lc code=start
class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        xor = 0

        if len(nums2) % 2:
            for n1 in nums1:
                xor ^= n1

        if len(nums1) % 2:
            for n2 in nums2:
                xor ^= n2

        return xor


# @lc code=end
