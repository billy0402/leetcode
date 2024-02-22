#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#


# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if not trust and n == 1:
            return 1

        hash_table: dict[int, int] = {}

        for person, trusted in trust:
            hash_table[person] = hash_table.get(person, 0) - 1
            hash_table[trusted] = hash_table.get(trusted, 0) + 1

        for key, value in hash_table.items():
            if value == n - 1:
                return key

        return -1


# @lc code=end
