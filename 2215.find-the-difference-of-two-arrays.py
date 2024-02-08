#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#


# @lc code=start
class Solution:
    def findDifference(
        self,
        nums1: list[int],
        nums2: list[int],
    ) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


# @lc code=end
