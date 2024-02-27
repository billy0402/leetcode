#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def travel(node: Optional[TreeNode]):
            nonlocal diameter

            if node is None:
                return 0

            left = travel(node.left)
            right = travel(node.right)
            diameter = max(diameter, left + right)
            return 1 + max(left, right)

        diameter = 0
        travel(root)
        return diameter


# @lc code=end
