#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
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
    def flipEquiv(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        queue = deque([(root1, root2)])

        while len(queue):
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            if (node1.left and node2.left and node1.left.val == node2.left.val) or (
                not node1.left and not node2.left
            ):  # not flip
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            else:  # flip
                queue.append((node1.left, node2.right))
                queue.append((node1.right, node2.left))

        return True


# @lc code=end
