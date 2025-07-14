#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        result = 0
        while head:
            # << 進一位(x2), | 加入最後一位
            result = (result << 1) | head.val
            head = head.next
        return result


# @lc code=end
