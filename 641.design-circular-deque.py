#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class MyCircularDeque:
    def __init__(self, k: int):
        self.deque: list[int] = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.deque.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.deque.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.deque.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.deque.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(3)
# print(obj.insertLast(1))
# print(obj.insertLast(2))
# print(obj.insertFront(3))
# print(obj.insertFront(4))
# print(obj.getRear())
# print(obj.isFull())
# print(obj.deleteLast())
# print(obj.insertFront(4))
# print(obj.getFront())
# @lc code=end
