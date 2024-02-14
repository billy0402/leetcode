#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#


# @lc code=start
class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answers = [0] * length
        positive_index, negative_index = 0, 1

        for n in nums:
            if n > 0:
                answers[positive_index] = n
                positive_index += 2
            else:
                answers[negative_index] = n
                negative_index += 2

        return answers


# @lc code=end
