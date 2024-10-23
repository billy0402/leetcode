#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        queue: deque[tuple[TreeNode | None, TreeNode | None]] = deque([(root, None)])

        while queue:
            x_parent = y_parent = None

            for _ in range(len(queue)):
                current, parent = queue.popleft()
                if not current:
                    continue

                if current.val == x:
                    x_parent = parent
                if current.val == y:
                    y_parent = parent

                if current.left:
                    queue.append((current.left, current))
                if current.right:
                    queue.append((current.right, current))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False

        return False


# @lc code=end
