#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#


# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        counter = 0
        current_sum = 0
        # {prefix: number of occurrence}
        freq = {}  # To store the occurrence of prefix sums

        for num in nums:
            current_sum += num
            if current_sum == goal:
                counter += 1

            # Check if there is any prefix sum that can be subtracted
            # from the current sum to get the desired goal
            if current_sum - goal in freq:
                counter += freq[current_sum - goal]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return counter


# @lc code=end
