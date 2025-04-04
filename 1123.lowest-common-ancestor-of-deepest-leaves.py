#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
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
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        # return (LCA, depth)  # noqa: ERA001
        def dfs(node: TreeNode | None, depth: int) -> tuple[TreeNode | None, int]:
            if not node:
                return (None, depth + 1)

            left_node, left_depth = dfs(node.left, depth + 1)
            right_node, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left_node, left_depth
            if left_depth < right_depth:
                return right_node, right_depth
            return node, left_depth  # left_depth == right_depth

        LCA, _ = dfs(root, 0)  # noqa: N806
        return LCA


# @lc code=end
