#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        yield self.val
        if self.next:
            yield from self.next

    def __str__(self):
        return '->'.join(map(str, self))


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# @lc code=end
