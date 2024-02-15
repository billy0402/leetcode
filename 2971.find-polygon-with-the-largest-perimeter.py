#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#


# @lc code=start
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        total = 0
        answer = -1
        for n in nums:
            if n < total:
                answer = total + n
            total += n

        return answer


# @lc code=end
