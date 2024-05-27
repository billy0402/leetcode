#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)

        frequencies = [0] * (n + 1)
        for num in nums:
            frequencies[min(num, n)] += 1

        counter = 0
        for i in range(n, 0, -1):
            counter += frequencies[i]

            if i == counter:
                return i

        return -1


# @lc code=end
