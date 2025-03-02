#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#

# @lc code=start
class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        results: list[list[int]] = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                results.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                results.append(nums1[i])
                i += 1
            else:  # nums1[i][0] > nums2[j][0]
                results.append(nums2[j])
                j += 1

        while i < len(nums1):
            results.append(nums1[i])
            i += 1

        while j < len(nums2):
            results.append(nums2[j])
            j += 1

        return results


# @lc code=end
