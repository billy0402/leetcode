#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen: set[int] = set()
        for n in arr:
            if n * 2 in seen or n / 2 in seen:
                return True
            seen.add(n)
        return False


# @lc code=end
