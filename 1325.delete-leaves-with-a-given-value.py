#
# @lc app=leetcode id=1325 lang=python3
#
# [1325] Delete Leaves With a Given Value
#

# @lc code=start
from typing import Self


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
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        if root is None:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.left is None and root.right is None and root.val == target:
            return None

        return root


# @lc code=end
