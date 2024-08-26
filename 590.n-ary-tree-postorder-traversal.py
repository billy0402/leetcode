#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
from typing import Self


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, children: list[Self] | None = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def postorder(self, root: Node) -> list[int]:
        def helper(node: Node | None):
            if not node:
                return

            for child in node.children:
                helper(child)

            result.append(node.val)

        result: list[int] = []
        helper(root)
        return result


# @lc code=end
