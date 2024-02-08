#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
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
    def searchBST(
        self,
        root: Optional[TreeNode],
        val: int,
    ) -> Optional[TreeNode]:
        def traverse(node: TreeNode):
            if not node:
                return None
            elif val < node.val:
                return traverse(node.left)
            elif val > node.val:
                return traverse(node.right)
            else:
                return node

        return traverse(root)


# @lc code=end
