#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        nodes: dict[int, TreeNode] = {}
        children: set[int] = set()

        for p, c, is_left in descriptions:
            child = nodes[c] if c in nodes else TreeNode(c)
            parent = nodes[p] if p in nodes else TreeNode(p)

            if is_left:
                parent.left = child
            else:
                parent.right = child

            nodes[p] = parent
            nodes[c] = child

            children.add(c)

        for p, _, _ in descriptions:
            if p not in children:
                return nodes[p]

        return None


# @lc code=end
