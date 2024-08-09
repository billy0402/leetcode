#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        seen: set[int] = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
        return -1


# @lc code=end
