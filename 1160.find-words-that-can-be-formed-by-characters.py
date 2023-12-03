#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
from typing import List


class Solution:
    def word_counter(self, text: str):
        map = {}
        for char in text:
            if char not in map:
                map[char] = text.count(char)
        return map

    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0

        m_chars = self.word_counter(chars)

        for word in words:
            m_word = self.word_counter(word)

            if all(
                m_chars.get(word, 0) >= counter
                for word, counter in m_word.items()
            ):
                length += len(word)

        return length


# @lc code=end
