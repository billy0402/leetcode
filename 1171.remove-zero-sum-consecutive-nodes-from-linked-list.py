#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefix_sum = 0
        prefix_sum_to_node = {0: dummy}
        current = head
        while current:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        prefix_sum = 0
        current = dummy
        while current:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        return dummy.next


# @lc code=end
