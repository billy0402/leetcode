#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#


# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        frequencies: dict[int, int] = {}
        max_frequency = 0
        total_frequency = 0

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            frequency = frequencies[num]

            if frequency > max_frequency:
                max_frequency = frequency
                total_frequency = frequency
            elif frequency == max_frequency:
                total_frequency += frequency

        return total_frequency


# @lc code=end
