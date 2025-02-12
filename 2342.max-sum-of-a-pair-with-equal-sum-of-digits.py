#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start
from collections import defaultdict


class Solution:
    def calculate_digit_sum(self, num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        return digit_sum

    def maximumSum(self, nums: list[int]) -> int:
        digit_sums: list[int] = []
        digit_sum_pairs: dict[int, list[int]] = defaultdict(list)
        for num in nums:
            digit_sum = self.calculate_digit_sum(num)
            digit_sums.append(digit_sum)
            digit_sum_pairs[digit_sum].append(num)

        max_pair_sum = -1
        for group_nums in digit_sum_pairs.values():
            if len(group_nums) < 2:  # noqa: PLR2004
                continue
            group_nums.sort(reverse=True)
            max_pair_sum = max(max_pair_sum, group_nums[0] + group_nums[1])
        return max_pair_sum


# @lc code=end
