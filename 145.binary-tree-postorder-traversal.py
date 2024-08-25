#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Self


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Self | None = None,
        right: Self | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        def post_order(node: TreeNode | None):
            if not node:
                return

            post_order(node.left)
            post_order(node.right)

            result.append(node.val)

        result: list[int] = []
        post_order(root)
        return result


# @lc code=end
