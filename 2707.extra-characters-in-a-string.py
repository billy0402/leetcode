#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_word = False


class Trie:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for word in words:
            current = self.root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.is_word = True


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n, trie = len(s), Trie(dictionary)
        dp: dict[int, int] = {n: 0}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]

            # skip current char
            extra = dfs(i + 1) + 1
            node = trie.root

            for j in range(i, n):
                if s[j] not in node.children:
                    break

                node = node.children[s[j]]
                if node.is_word:
                    extra = min(dfs(j + 1), extra)

            dp[i] = extra
            return extra

        return dfs(0)


# @lc code=end
