#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        q = deque([root])
        results: list[int] = []

        while q:
            current_max: int = float("-inf")  # pyright: ignore[reportAssignmentType]

            for _ in range(len(q)):
                node = q.popleft()
                current_max = max(current_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            results.append(current_max)

        return results


# @lc code=end
