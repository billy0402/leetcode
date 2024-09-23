#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

# @lc code=start
class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n, words = len(s), set(dictionary)
        dp: dict[int, int] = {n: 0}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]

            # skip current char
            extra = dfs(i + 1) + 1

            for j in range(i, n):
                if s[i : j + 1] in words:
                    extra = min(dfs(j + 1), extra)

            dp[i] = extra
            return extra

        return dfs(0)


# @lc code=end
