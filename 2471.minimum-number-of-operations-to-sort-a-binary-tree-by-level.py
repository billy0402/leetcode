#
# @lc app=leetcode id=2471 lang=python3
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
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
    def minimumOperations(self, root: TreeNode) -> int:
        def count_swaps(nums: list[int]) -> int:
            swaps = 0
            sorted_nums = sorted(nums)
            index_map = {n: i for i, n in enumerate(nums)}

            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    j = index_map[sorted_nums[i]]
                    nums[i], nums[j] = nums[j], nums[i]
                    index_map[nums[i]], index_map[nums[j]] = i, j
                    swaps += 1

            return swaps

        q = deque([root])
        counter = 0

        while q:
            level: list[int] = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            counter += count_swaps(level)

        return counter


# @lc code=end
