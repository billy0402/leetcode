#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
from typing import List

keyboards = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']


def isRowWord(word: str) -> bool:
    row = 0
    for i in range(len(keyboards)):
        if word[0] in keyboards[i]:
            row = i

    for c in word:
        if c not in keyboards[row]:
            return False
    return True


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result: List[str] = []
        for word in words:
            if isRowWord(word.lower()):
                result.append(word)
        return result


# @lc code=end
