#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
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
    results = []

    def tree2str(self, root: Optional[TreeNode]) -> str:
        def pre(node: Optional[TreeNode]):
            if node is None:
                return

            if node.val is not None:
                self.results.append(str(node.val))

            if node.left is None and node.right is None:
                return

            self.results.append('(')
            pre(node.left)
            self.results.append(')')

            if node.right is not None:
                self.results.append('(')
                pre(node.right)
                self.results.append(')')

        self.results = []
        pre(root)
        return ''.join(self.results)


# @lc code=end
