#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counter: dict[str, int] = {}
        for word in s1.split():
            counter[word] = counter.get(word, 0) + 1
        for word in s2.split():
            counter[word] = counter.get(word, 0) + 1
        return [key for key, value in counter.items() if value == 1]


# @lc code=end
