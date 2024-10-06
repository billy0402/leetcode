#
# @lc app=leetcode id=1813 lang=python3
#
# [1813] Sentence Similarity III
#

# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split(" ")
        w2 = sentence2.split(" ")

        if len(w2) < len(w1):
            w1, w2 = w2, w1
        n1, n2 = len(w1), len(w2)

        # prefix
        l1 = 0
        while l1 < n1 and w1[l1] == w2[l1]:
            l1 += 1

        # suffix
        r1, r2 = n1 - 1, n2 - 1
        while r1 >= l1 and r2 >= 0 and w1[r1] == w2[r2]:
            r1 -= 1
            r2 -= 1

        return l1 > r1


# @lc code=end
