#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#


# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        left = 0
        counter: dict[int, int] = {}
        max_length = 0

        for right in range(len(nums)):
            n = nums[right]
            counter[n] = counter.get(n, 0) + 1

            while counter[n] > k:
                counter[nums[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


# @lc code=end
