#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# word = "apple"
# obj.insert(word)
# param_2 = obj.search(word)
# print(param_2)
# prefix = "app"
# param_3 = obj.startsWith(prefix)
# print(param_3)
# @lc code=end
