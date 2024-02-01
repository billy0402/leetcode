#
# @lc app=leetcode id=2016 lang=python3
#
# [2016] Maximum Difference Between Increasing Elements
#


# @lc code=start
class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        answer = -1
        smallest = float('inf')

        for n in nums:
            if n > smallest:
                answer = max(answer, n - smallest)
            else:
                smallest = n

        return answer


# @lc code=end
