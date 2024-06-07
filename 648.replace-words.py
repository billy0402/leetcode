#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort()

        words = sentence.split(" ")

        for i in range(len(words)):
            for root in dictionary:
                if words[i].startswith(root):
                    words[i] = root
                    break

        return " ".join(words)


# @lc code=end
