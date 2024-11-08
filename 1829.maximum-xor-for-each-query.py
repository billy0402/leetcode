#
# @lc app=leetcode id=1829 lang=python3
#
# [1829] Maximum XOR for Each Query
#

# @lc code=start
class Solution:
    def getMaximumXor(self, nums: list[int], maximum_bit: int) -> list[int]:
        xor = 0
        for n in nums:
            xor ^= n

        results: list[int] = []
        mask = (2**maximum_bit) - 1
        for n in reversed(nums):
            results.append(xor ^ mask)
            xor ^= n

        return results


# @lc code=end
