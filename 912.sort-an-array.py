#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(l: int, m: int, r: int):
            left, right = nums[l : m + 1], nums[m + 1 : r + 1]
            i, j, k = 0, 0, l
            nl, nr = len(left), len(right)

            while i < nl and j < nr:
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < nl:
                nums[k] = left[i]
                i += 1
                k += 1

            while j < nr:
                nums[k] = right[j]
                j += 1
                k += 1

        def merge_sort(l: int, r: int):
            if l == r:
                return nums

            m = (l + r) // 2
            merge_sort(l, m)
            merge_sort(m + 1, r)
            merge(l, m, r)

        merge_sort(0, len(nums) - 1)
        return nums


# @lc code=end
