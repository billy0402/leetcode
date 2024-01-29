#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from typing import Generic, TypeVar

T = TypeVar('T')


class Stack(Generic[T]):
    stack: list[T]

    def __init__(self) -> None:
        self.stack = []

    @property
    def empty(self) -> bool:
        return not self.stack

    def append(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> T:
        return self.stack.pop()


class MyQueue:
    stack_in: Stack[int]
    stack_out: Stack[int]

    def __init__(self):
        self.stack_in = Stack[int]()
        self.stack_out = Stack[int]()

    def push(self, value: int) -> None:
        self.stack_in.append(value)

    def pop(self) -> int:
        if self.stack_out.empty:
            while not self.stack_in.empty:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        item = self.pop()
        self.stack_out.append(item)
        return item

    def empty(self) -> bool:
        return self.stack_in.empty and self.stack_out.empty


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
