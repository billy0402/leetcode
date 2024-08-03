#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Subarrays
#

# @lc code=start
class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        freq: dict[int, int] = {}
        for n in target:
            freq[n] = freq.get(n, 0) + 1

        for n in arr:
            if n not in freq:
                return False

            freq[n] -= 1
            if freq[n] == 0:
                del freq[n]

        return True


# @lc code=end
