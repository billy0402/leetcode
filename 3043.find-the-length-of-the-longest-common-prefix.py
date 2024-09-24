#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}


class Trie:
    def __init__(self, nums: list[int]) -> None:
        self.root = TrieNode()
        for num in nums:
            current = self.root
            for digit in str(num):
                if digit not in current.children:
                    current.children[digit] = TrieNode()
                current = current.children[digit]


class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie = Trie(arr1)

        longest_prefix = 0
        for num in arr2:
            current = trie.root
            value = str(num)
            temp_prefix = 0
            for digit in value:
                if digit not in current.children:
                    break
                temp_prefix += 1
                current = current.children[digit]
            longest_prefix = max(temp_prefix, longest_prefix)
        return longest_prefix


# @lc code=end
