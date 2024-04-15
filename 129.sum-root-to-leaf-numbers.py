#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path_sum: int) -> int:
            if node is None:
                return 0

            path_sum = path_sum * 10 + node.val

            if node.left is None and node.right is None:
                return path_sum
            return dfs(node.left, path_sum) + dfs(node.right, path_sum)

        return dfs(root, 0)


# @lc code=end
