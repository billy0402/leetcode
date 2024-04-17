#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode], current: str) -> str:
            if node is None:
                return ''

            current = chr(ord('a') + node.val) + current

            if node.left is not None and node.right is not None:
                return min(dfs(node.left, current), dfs(node.right, current))
            elif node.left is not None:
                return dfs(node.left, current)
            elif node.right is not None:
                return dfs(node.right, current)

            return current

        return dfs(root, '')


# @lc code=end
