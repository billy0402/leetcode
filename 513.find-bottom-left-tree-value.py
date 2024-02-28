#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def travel(node: Optional[TreeNode], depth=0):
            nonlocal left_most
            nonlocal max_depth

            if node is None or node.val is None:
                return

            if depth > max_depth:
                left_most = node.val
                max_depth = depth

            travel(node.left, depth + 1)
            travel(node.right, depth + 1)

        left_most = -1
        max_depth = -1
        travel(root)
        return left_most


# @lc code=end
