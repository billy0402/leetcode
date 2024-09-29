#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
import typing as t


class ListNode:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev = self.next = t.cast(ListNode, None)


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, ListNode] = {}
        self.linked_list = DoublyLinkedList()

    def insert_node(self, node: ListNode):
        prev, next_ = self.linked_list.tail.prev, self.linked_list.tail
        prev.next = next_.prev = node
        node.next, node.prev = next_, prev

    def remove_node(self, node: ListNode):
        prev, next_ = node.prev, node.next
        prev.next, next_.prev = next_, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove_node(self.cache[key])
        self.insert_node(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.linked_list.head.next
            self.remove_node(lru)
            self.cache.pop(lru.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))
# @lc code=end
