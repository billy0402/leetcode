#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    results = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def in_oder(node: Optional[TreeNode]):
            if node is None:
                return

            in_oder(node.left)

            if node.val is not None:
                self.results.append(node.val)

            in_oder(node.right)

        self.results = []
        in_oder(root)
        return self.results


# @lc code=end
