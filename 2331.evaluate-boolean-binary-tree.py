#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
from typing import Self

FALSE = 0
TRUE = 1
OR = 2
AND = 3


# Definition for a binary tree node.
class TreeNode:
    val: int
    left: Self | None
    right: Self | None

    def __init__(self, val=0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, node: TreeNode | None) -> bool:
        if not node:
            return False

        if not node.left and not node.right:
            return node.val != FALSE

        left = self.evaluateTree(node.left)
        right = self.evaluateTree(node.right)

        return left or right if node.val == OR else left and right


# @lc code=end
