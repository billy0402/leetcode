#
# @lc app=leetcode id=2161 lang=python3
#
# [2161] Partition Array According to Given Pivot
#

# @lc code=start
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n = len(nums)
        results: list[int] = [pivot] * n
        i2, j2 = 0, n - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1), strict=True):
            if nums[i] < pivot:
                results[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                results[j2] = nums[j]
                j2 -= 1

        return results


# @lc code=end
