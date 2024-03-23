#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack: list[int] = []

        current = head
        while current is not None:
            stack.append(current)
            current = current.next

        current = head
        middle = len(stack) // 2
        for _ in range(middle):
            next = current.next
            new_node = stack.pop()
            new_node.next = next
            current.next = new_node
            current = next

        current.next = None


# @lc code=end
