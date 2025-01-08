#
# @lc app=leetcode id=3045 lang=python3
#
# [3045] Count Prefix and Suffix Pairs II
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[tuple[str, str], TrieNode] = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        current = self.root
        for prefix, suffix in zip(word, reversed(word), strict=True):
            current = current.children.setdefault((prefix, suffix), TrieNode())
            current.count += 1

    def count(self, word: str) -> int:
        current = self.root
        for prefix, suffix in zip(word, reversed(word), strict=True):
            if (prefix, suffix) not in current.children:
                return 0
            current = current.children[(prefix, suffix)]
        return current.count


class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        counter = 0
        trie = Trie()

        for word in reversed(words):
            counter += trie.count(word)
            trie.add(word)

        return counter


# @lc code=end
