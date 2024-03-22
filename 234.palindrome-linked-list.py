#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        previous: Optional[ListNode] = None

        while fast and fast.next:
            fast = fast.next.next

            next = slow.next
            slow.next = previous
            previous, slow = slow, next

        if fast is not None:
            slow = slow.next

        while previous and slow:
            if previous.val != slow.val:
                return False

            previous = previous.next
            slow = slow.next

        return True


# @lc code=end
