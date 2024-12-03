#
# @lc app=leetcode id=2109 lang=python3
#
# [2109] Adding Spaces to a String
#

# @lc code=start
class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        results: list[str] = []
        space_index = 0

        for i, char in enumerate(s):
            if space_index < len(spaces) and i == spaces[space_index]:
                results.append(" ")
                space_index += 1

            results.append(char)

        return "".join(results)


# @lc code=end
