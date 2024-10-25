#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_folder = False


class Trie:
    def __init__(self, paths: list[str]) -> None:
        self.root = TrieNode()
        for path in paths:
            current = self.root
            folders = path.split("/")
            for name in folders:
                if name not in current.children:
                    current.children[name] = TrieNode()
                current = current.children[name]
            current.is_end_of_folder = True

    def has_parent(self, path: str) -> bool:
        current = self.root
        folders = path.split("/")
        for i, name in enumerate(folders):
            current = current.children[name]
            if current.is_end_of_folder and i != len(folders) - 1:
                return True
        return False


class Solution:
    def removeSubfolders(self, folders: list[str]) -> list[str]:
        trie = Trie(folders)
        return [path for path in folders if not trie.has_parent(path)]


# @lc code=end
