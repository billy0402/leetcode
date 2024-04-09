#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        results: list[str] = []
        left = right = 0

        while right < len(nums):
            if right < len(nums) - 1 and nums[right + 1] - nums[right] == 1:
                right += 1
            else:
                if left == right:
                    results.append(f'{nums[left]}')
                else:
                    results.append(f'{nums[left]}->{nums[right]}')

                right += 1
                left = right

        return results


# @lc code=end
