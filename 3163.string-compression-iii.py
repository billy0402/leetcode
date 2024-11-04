#
# @lc app=leetcode id=3163 lang=python3
#
# [3163] String Compression III
#

# @lc code=start
MAX_REPEATING = 9


class Solution:
    def compressedString(self, word: str) -> str:
        comp: list[str] = []

        i = 0
        while i < len(word):
            char, counter = word[i], 0
            while i < len(word) and char == word[i] and counter < MAX_REPEATING:
                i += 1
                counter += 1

            comp.append(str(counter))
            comp.append(char)

        return "".join(comp)


# @lc code=end
