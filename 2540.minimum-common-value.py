#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#


# @lc code=start
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        first = 0
        second = 0

        while first < len(nums1) and second < len(nums2):
            n1 = nums1[first]
            n2 = nums2[second]

            if n1 < n2:
                first += 1
            elif n1 > n2:
                second += 1
            else:
                return n1

        return -1


# @lc code=end
