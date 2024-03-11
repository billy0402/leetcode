#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#


# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hash_table: dict[str, int] = {}
        answer: list[str] = []

        for char in s:
            hash_table[char] = hash_table.get(char, 0) + 1

        for char in order:
            value = hash_table.get(char)
            if not value:
                continue

            for _ in range(value):
                answer.append(char)
            del hash_table[char]

        for key, value in hash_table.items():
            for _ in range(value):
                answer.append(key)

        return ''.join(answer)


# @lc code=end
