#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#


# @lc code=start
class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        answer: list[int] = []
        nums.sort()

        for i in range(0, len(nums), 3):
            n1 = nums[i]
            n2 = nums[i + 1]
            n3 = nums[i + 2]
            if n3 - n1 > k:
                return []
            answer.append([n1, n2, n3])

        return answer


# @lc code=end
