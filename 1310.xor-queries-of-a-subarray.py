#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]

        result: list[int] = []
        for left, right in queries:
            total = arr[right]
            remove = arr[left - 1] if left > 0 else 0
            result.append(total ^ remove)
        return result


# @lc code=end
