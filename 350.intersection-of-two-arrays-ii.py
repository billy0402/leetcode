#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        hash_table: dict[int, int] = {}
        for n in nums2:
            hash_table[n] = hash_table.get(n, 0) + 1

        intersection: list[int] = []
        for n in nums1:
            if n in hash_table and hash_table[n]:
                intersection.append(n)
                hash_table[n] -= 1

        return intersection


# @lc code=end
