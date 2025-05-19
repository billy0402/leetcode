#
# @lc app=leetcode id=3024 lang=python3
#
# [3024] Type of Triangle
#

# @lc code=start
class Solution:
    def triangleType(self, nums: list[int]) -> str:
        nums.sort()

        s1, s2, s3 = nums
        if s1 == s2 == s3:
            return "equilateral"
        if s1 + s2 > s3:
            if s2 in (s1, s3):
                return "isosceles"
            return "scalene"
        return "none"


# @lc code=end
