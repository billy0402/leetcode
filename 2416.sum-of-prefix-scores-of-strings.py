#
# @lc app=leetcode id=2416 lang=python3
#
# [2416] Sum of Prefix Scores of Strings
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, value: str):
        current = self.root
        for char in value:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.counter += 1

    def sum_of_prefix_scores(self, value: str) -> int:
        current = self.root
        counter = 0
        for char in value:
            current = current.children[char]
            counter += current.counter
        return counter


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        scores: list[int] = []
        for word in words:
            score = trie.sum_of_prefix_scores(word)
            scores.append(score)
        return scores


# @lc code=end
