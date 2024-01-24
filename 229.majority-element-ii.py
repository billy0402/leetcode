#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        major1, major2 = -1, -1
        count1, count2 = 0, 0

        for n in nums:
            if n == major1:
                count1 += 1
            elif n == major2:
                count2 += 1
            elif count1 == 0:
                major1 = n
                count1 = 1
            elif count2 == 0:
                major2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0
        for n in nums:
            if n == major1:
                count1 += 1
            elif n == major2:
                count2 += 1

        answers = []
        min_count = len(nums) // 3
        if count1 > min_count:
            answers.append(major1)
        if count2 > min_count:
            answers.append(major2)
        return answers


# @lc code=end
