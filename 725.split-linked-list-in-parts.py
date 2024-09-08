#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
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
    def splitListToParts(
        self,
        head: ListNode | None,
        k: int,
    ) -> list[ListNode | None]:
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        average, remaining = divmod(size, k)

        result: list[ListNode | None] = [None] * k
        current = head
        for i in range(k):
            split_size = average
            if remaining > 0:
                split_size += 1
                remaining -= 1

            part_head = current
            for _ in range(split_size - 1):
                if not current:
                    break
                current = current.next

            if current:
                next_part = current.next
                current.next = None
                current = next_part

            result[i] = part_head

        return result


# @lc code=end
