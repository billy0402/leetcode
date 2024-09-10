#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
import math
import typing as t


# Definition for singly-linked list.
class ListNode:
    val: int
    next: t.Self | None

    def __init__(self, val: int = 0, next_: t.Self | None = None):
        self.val = val
        self.next = next_


class Solution:
    def insertGreatestCommonDivisors(
        self,
        head: ListNode | None,
    ) -> ListNode | None:
        current = head

        while current and current.next:
            gcd = math.gcd(current.val, current.next.val)
            next_node = current.next
            gcd_node = ListNode(gcd, next_node)
            current.next = gcd_node
            current = next_node

        return head


# @lc code=end
