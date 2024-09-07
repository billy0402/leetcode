#
# @lc app=leetcode id=1367 lang=python3
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
import typing as t


# Definition for singly-linked list.
class ListNode:
    val: int
    next: t.Self | None

    def __init__(self, val: int = 0, next_: t.Self | None = None):
        self.val = val
        self.next = next_


# Definition for a binary tree node.
class TreeNode:
    val: int
    left: t.Self | None
    right: t.Self | None

    def __init__(
        self,
        val: int = 0,
        left: t.Self | None = None,
        right: t.Self | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode | None, root: TreeNode | None) -> bool:
        if not root:
            return False
        if self.compare(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def compare(self, list_node: ListNode | None, tree_node: TreeNode | None) -> bool:
        if not list_node:
            return True
        if not tree_node or list_node.val != tree_node.val:
            return False
        return self.compare(list_node.next, tree_node.left) or self.compare(
            list_node.next,
            tree_node.right,
        )


# @lc code=end
