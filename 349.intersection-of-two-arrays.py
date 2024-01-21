#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#


# @lc code=start
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set2) < len(set1):
            return list(set2.intersection(set1))

        return list(set1.intersection(set2))


# @lc code=end
