#
# @lc app=leetcode id=2326 lang=python3
#
# [2326] Spiral Matrix IV
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
    def spiralMatrix(self, m: int, n: int, head: ListNode | None) -> list[list[int]]:
        rows, cols = m, n
        r, c = 0, -1
        direction = 1  # 1 or -1
        result = [([-1] * cols) for _ in range(rows)]
        i = 1

        while rows and cols:
            for _ in range(cols):
                if not head:
                    break

                # 1 is right, -1 is left
                c += direction
                result[r][c] = head.val
                head = head.next
                i += 1
            rows -= 1

            for _ in range(rows):
                if not head:
                    break

                # 1 is bottom, -1 is top
                r += direction
                result[r][c] = head.val
                head = head.next
                i += 1
            cols -= 1

            direction *= -1

        return result


# @lc code=end
