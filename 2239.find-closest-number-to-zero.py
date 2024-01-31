#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
MAX_N = 100001


class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        answer = MAX_N
        closest = MAX_N
        for n in nums:
            if abs(n) < closest:
                answer = n
                closest = abs(answer)
            elif abs(n) == closest:
                answer = max(answer, n)
        return answer


# @lc code=end
