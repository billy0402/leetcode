#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#


# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) \
            -> list[int]:
        hash_table: dict[int, int] = {}
        stack: list[int] = []

        for n in nums2:
            while stack and n > stack[-1]:
                top = stack.pop()
                hash_table[top] = n
            stack.append(n)

        return [hash_table.get(n, -1) for n in nums1]


# @lc code=end
