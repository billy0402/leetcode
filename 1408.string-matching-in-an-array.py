#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.frequency = 0


class Trie:
    def __init__(self, words: list[str]) -> None:
        self.root = TrieNode()
        for word in words:
            for i in range(len(word)):
                current = self.root
                for char in word[i:]:
                    current = current.children.setdefault(char, TrieNode())
                    current.frequency += 1

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.frequency > 1


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        trie = Trie(words)
        return [word for word in words if trie.search(word)]


# @lc code=end
