#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
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
    total = 0

    def rangeSumBST(
        self,
        root: Optional[TreeNode],
        low: int,
        high: int,
    ) -> int:
        def pre_order(node: TreeNode):
            if not node:
                return

            if low <= node.val <= high:
                self.total += node.val
                pre_order(node.left)
                pre_order(node.right)

            elif node.val < low:
                pre_order(node.right)

            elif node.val > high:
                pre_order(node.left)

        self.total = 0
        pre_order(root)
        return self.total


# @lc code=end
