#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#


# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        hash_table: dict[str, int] = {}
        for char in s:
            hash_table[char] = hash_table.get(char, 0) + 1

        char_frequencies = sorted(hash_table.items(), key=lambda x: -x[1])

        answers: list[str] = []
        for char, frequency in char_frequencies:
            answers.append(char * frequency)
        return ''.join(answers)


# @lc code=end
