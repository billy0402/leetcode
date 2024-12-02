#
# @lc app=leetcode id=1346 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
#

# @lc code=start
class TrieNode:
    def __init__(self, index: int | None = None) -> None:
        self.index = index
        self.children: dict[str, TrieNode] = {}


class Trie:
    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        for i, word in enumerate(words):
            current = self.root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode(i + 1)
                current = current.children[char]

    def startswith(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return -1
            current = current.children[char]
        return current.index or -1


class Solution:
    def isPrefixOfWord(self, sentence: str, search_word: str) -> int:
        words = sentence.split(" ")
        trie = Trie(words)
        return trie.startswith(search_word)


# @lc code=end
