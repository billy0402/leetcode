#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#


# @lc code=start
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        def set_intersection(set1: set, set2: set):
            return list(n for n in set1 if n in set2)

        set1 = set(nums1)
        set2 = set(nums2)

        if len(set2) > len(set1):
            return set_intersection(set2, set1)

        return set_intersection(set1, set2)


# @lc code=end
