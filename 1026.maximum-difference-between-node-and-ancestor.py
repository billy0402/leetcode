#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
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
    max_difference = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if node is None or node.val is None:
                return float('-inf'), float('inf')

            left_max, left_min = dfs(node.left)
            right_max, right_min = dfs(node.right)

            ma = max(node.val, left_max, right_max)
            mi = min(node.val, left_min, right_min)

            self.max_difference = max(
                self.max_difference,
                abs(node.val - ma),
                abs(node.val - mi),
            )

            return ma, mi

        self.max_difference = 0
        dfs(root)
        return self.max_difference


# @lc code=end
