#
# @lc app=leetcode id=3375 lang=python3
#
# [3375] Minimum Operations to Make Array Values Equal to K
#

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        greater: set[int] = set()

        for n in nums:
            if n < k:
                return -1
            if n > k:
                greater.add(n)

        return len(greater)


# @lc code=end
