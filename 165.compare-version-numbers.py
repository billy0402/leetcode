#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#


# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        length = max(len(nums1), len(nums2))

        for i in range(length):
            v1 = int(nums1[i]) if i < len(nums1) else 0
            v2 = int(nums2[i]) if i < len(nums2) else 0

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0


# @lc code=end
