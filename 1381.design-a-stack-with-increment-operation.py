#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:
    def __init__(self, max_size: int):
        self.stack: list[int] = []
        self.max_size = max_size

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return

        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(3)
# obj.push(1)
# obj.push(2)
# print(obj.pop())
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.increment(5, 100)
# obj.increment(2, 100)
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# print(obj.pop())
# @lc code=end
