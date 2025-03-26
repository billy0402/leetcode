#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # Ensure all remainders are equal.
        remainder = grid[0][0] % x
        for row in grid:
            for n in row:
                if n % x != remainder:
                    return -1

        # Flatten and sort the grid.
        nums = [n for row in grid for n in row]
        nums.sort()

        # Use prefix sum and suffix sum to calculate the minimum operations.
        min_operations: int = float("inf")  # pyright: ignore[reportAssignmentType]
        total = sum(nums)
        prefix_sum = 0
        for i in range(len(nums)):
            cost_left = nums[i] * i - prefix_sum
            cost_right = total - prefix_sum - nums[i] * (len(nums) - i)
            operations = (cost_left + cost_right) // x
            min_operations = min(min_operations, operations)
            prefix_sum += nums[i]
        return min_operations


# @lc code=end
