#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
WORD = 'balon'


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_table = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0,
        }

        for char in text:
            if char in hash_table:
                hash_table[char] += 1

        return min(
            hash_table['b'],
            hash_table['a'],
            hash_table['l'] // 2,
            hash_table['o'] // 2,
            hash_table['n'],
        )


# @lc code=end
