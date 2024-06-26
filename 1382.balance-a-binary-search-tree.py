#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def in_order_traversal(node: TreeNode | None):
            if node is None or node.val is None:
                return

            in_order_traversal(node.left)
            in_order.append(node.val)
            in_order_traversal(node.right)

        def create_balance_BST(start: int, end: int) -> TreeNode | None:
            if start > end:
                return None

            middle = start + (end - start) // 2
            left_subtree = create_balance_BST(start, middle - 1)
            right_subtree = create_balance_BST(middle + 1, end)
            tree = TreeNode(in_order[middle], left_subtree, right_subtree)
            return tree

        in_order: list[int] = []
        in_order_traversal(root)
        tree = create_balance_BST(0, len(in_order) - 1)
        if tree is None:
            return TreeNode()
        return tree


# @lc code=end
