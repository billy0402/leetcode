#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
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


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode | None:
        num_set = set(nums)
        dummy = ListNode(next_=head)

        current = dummy
        while current.next:
            if current.next.val in num_set:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


# @lc code=end
