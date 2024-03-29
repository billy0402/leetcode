#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        ans = start = max_num_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_num:
                max_num_in_window += 1

            while max_num_in_window == k:
                if nums[start] == max_num:
                    max_num_in_window -= 1
                start += 1

            ans += start

        return ans


# @lc code=end
