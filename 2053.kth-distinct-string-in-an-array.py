#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counter: dict[str, int] = {}

        for s in arr:
            counter[s] = counter.get(s, 0) + 1

        for s in arr:
            if counter[s] == 1:
                k -= 1

                if k == 0:
                    return s

        return ""


# @lc code=end
