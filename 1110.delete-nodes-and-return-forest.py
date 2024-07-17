#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        def dfs(node: TreeNode | None):
            if not node:
                return None

            parent = node
            if node.val in should_delete:
                parent = None
                forest.discard(node)
                if node.left:
                    forest.add(node.left)
                if node.right:
                    forest.add(node.right)

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return parent

        forest = {root}
        should_delete = set(to_delete)
        dfs(root)
        return list(forest)


# @lc code=end
