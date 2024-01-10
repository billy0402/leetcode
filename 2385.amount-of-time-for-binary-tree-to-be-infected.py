#
# @lc app=leetcode id=2385 lang=python3
#
# [2385] Amount of Time for Binary Tree to Be Infected
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
    max_distance = 0

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def traverse(node) -> int:
            depth = 0
            if node is None:
                return depth

            left_depth = traverse(node.left)
            right_depth = traverse(node.right)

            # node is start
            if node.val == start:
                self.max_distance = max(left_depth, right_depth)
                depth = -1
            # node is root
            elif left_depth >= 0 and right_depth >= 0:
                depth = max(left_depth, right_depth) + 1
            # sub tree includes start
            else:
                # left + right
                distance = abs(left_depth) + abs(right_depth)
                # save the max
                self.max_distance = max(self.max_distance, distance)
                # negative = start to root
                depth = min(left_depth, right_depth) - 1

            return depth

        self.max_distance = 0
        traverse(root)
        return self.max_distance


# @lc code=end
