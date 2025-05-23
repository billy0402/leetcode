#
# @lc app=leetcode id=2490 lang=python3
#
# [2490] Circular Sentence
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        return all(words[i - 1][-1] == words[i][0] for i in range(len(words)))


# @lc code=end
