#
# @lc app=leetcode id=2641 lang=python3
#
# [2641] Cousins in Binary Tree II
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
    def replaceValueInTree(self, root: TreeNode | None = None) -> TreeNode | None:
        queue = deque([root])
        level_sums: list[int] = []
        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                current = queue.popleft()
                if not current:
                    continue

                level_sum += current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            level_sums.append(level_sum)

        queue = deque([root])
        level = 1
        if root:
            root.val = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if not current:
                    continue

                left_val = current.left.val if current.left else 0
                right_val = current.right.val if current.right else 0
                sibling_sum = left_val + right_val

                if current.left:
                    current.left.val = level_sums[level] - sibling_sum
                    queue.append(current.left)
                if current.right:
                    current.right.val = level_sums[level] - sibling_sum
                    queue.append(current.right)

            level += 1

        return root


# @lc code=end
