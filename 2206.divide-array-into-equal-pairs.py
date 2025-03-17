#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                seen.remove(n)
        return len(seen) == 0


# @lc code=end
