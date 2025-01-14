#
# @lc app=leetcode id=2657 lang=python3
#
# [2657] Find the Prefix Common Array of Two Arrays
#

# @lc code=start
class Solution:
    def findThePrefixCommonArray(
        self, list_a: list[int], list_b: list[int]
    ) -> list[int]:
        results: list[int] = []
        seen: set[int] = set()
        count = 0

        for a, b in zip(list_a, list_b, strict=True):
            if a in seen:
                count += 1
            seen.add(a)

            if b in seen:
                count += 1
            seen.add(b)

            results.append(count)

        return results


# @lc code=end
