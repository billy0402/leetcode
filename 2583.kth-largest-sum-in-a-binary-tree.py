#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
#

# @lc code=start
import heapq
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        queue = deque([root])
        min_heap: list[int] = []  # max size = k

        while len(queue) > 0:
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

            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return -1 if len(min_heap) < k else min_heap[0]


# @lc code=end
