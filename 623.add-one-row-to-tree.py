#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
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
    def addOneRow(
        self,
        root: Optional[TreeNode],
        val: int,
        depth: int,
    ) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], current_depth=1):
            if node is None or current_depth > depth:
                return

            if current_depth == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
                return

            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        if depth == 1:
            return TreeNode(val, root)
        dfs(root)
        return root


# @lc code=end
