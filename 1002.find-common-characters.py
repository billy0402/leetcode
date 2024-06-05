#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cnt = Counter(words[0])

        for i in range(1, len(words)):
            cur_cnt = Counter(words[i])
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        res: list[str] = []
        for c in cnt:
            for _ in range(cnt[c]):
                res.append(c)
        return res


# @lc code=end
