#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#

# @lc code=start
import typing as t
from collections import defaultdict

NONE_NODE = t.cast("ListNode", None)


class ListNode:
    def __init__(
        self,
        value: int,
        prev: t.Self = NONE_NODE,
        next_: t.Self = NONE_NODE,
    ):
        self.value = value
        self.prev, self.next = prev, next_


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head

        self.map: dict[int, ListNode] = {}

    def push(self, value: int):
        node = ListNode(value, self.tail.prev, self.tail)
        node.prev.next = node
        self.tail.prev = node

        self.map[value] = node

    def update(self, value: int):
        self.pop(value)
        self.push(value)

    def pop(self, value: int):
        if value not in self.map:
            return

        node = self.map[value]
        prev, next_ = node.prev, node.next
        prev.next, next_.prev = next_, prev

        self.map.pop(value)

    def pop_left(self):
        value = self.head.next.value
        self.pop(value)
        return value

    def __len__(self) -> int:
        return len(self.map)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_count = 0
        # key -> value
        self.value_map: dict[int, int] = {}
        # key -> count
        self.count_map: dict[int, int] = defaultdict(int)
        # count -> linked_list
        self.list_map: dict[int, DoublyLinkedList] = defaultdict(DoublyLinkedList)

    def count(self, key: int):
        count = self.count_map[key]
        self.count_map[key] += 1
        self.list_map[count].pop(key)
        self.list_map[count + 1].push(key)

        if count == self.lfu_count and not self.list_map[count]:
            self.lfu_count += 1

    def get(self, key: int) -> int:
        if key not in self.value_map:
            return -1

        self.count(key)
        return self.value_map[key]

    def put(self, key: int, value: int):
        if self.capacity == 0:
            return

        if key not in self.value_map and len(self.value_map) == self.capacity:
            left = self.list_map[self.lfu_count].pop_left()
            self.value_map.pop(left)
            self.count_map.pop(left)

        self.value_map[key] = value
        self.count(key)
        self.lfu_count = min(self.count_map[key], self.lfu_count)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# print(obj.get(3))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
# @lc code=end
