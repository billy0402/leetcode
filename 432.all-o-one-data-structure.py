#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#

# @lc code=start
import typing as t


class ListNode:
    def __init__(self, freq: int):
        self.freq = freq
        self.prev = self.next = t.cast(ListNode, None)
        self.keys: set[str] = set()


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head


class AllOne:
    def __init__(self):
        self.map: dict[str, ListNode] = {}
        self.linked_list = DoublyLinkedList()

    def remove_node(self, node: ListNode):
        prev, next_ = node.prev, node.next
        prev.next, next_.prev = next_, prev

    def inc(self, key: str) -> None:
        if key in self.map:
            node = self.map[key]
            node.keys.remove(key)

            next_node = node.next
            if next_node == self.linked_list.tail or next_node.freq != node.freq + 1:
                new_node = ListNode(node.freq + 1)
                new_node.prev, new_node.next = node, next_node
                new_node.keys.add(key)

                node.next = new_node
                next_node.prev = new_node
                self.map[key] = new_node
            else:
                next_node.keys.add(key)
                self.map[key] = next_node

            if not node.keys:
                self.remove_node(node)

        else:
            first_node = self.linked_list.head.next
            if first_node == self.linked_list.tail or first_node.freq > 1:
                new_node = ListNode(1)
                new_node.keys.add(key)
                new_node.prev, new_node.next = self.linked_list.head, first_node

                self.linked_list.head.next = new_node
                first_node.prev = new_node

                self.map[key] = new_node
            else:
                first_node.keys.add(key)
                self.map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)

        if node.freq == 1:
            self.map.pop(key)
        else:
            prev_node = node.prev
            if prev_node == self.linked_list.head or prev_node.freq != node.freq - 1:
                new_node = ListNode(node.freq - 1)
                new_node.prev, new_node.next = prev_node, node
                new_node.keys.add(key)

                prev_node.next = new_node
                node.prev = new_node
                self.map[key] = new_node
            else:
                prev_node.keys.add(key)
                self.map[key] = prev_node

        if not node.keys:
            self.remove_node(node)

    def getMaxKey(self) -> str:
        if self.linked_list.head.next == self.linked_list.tail:
            return ""

        return next(iter(self.linked_list.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.linked_list.head.next == self.linked_list.tail:
            return ""

        return next(iter(self.linked_list.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc("hello")
# obj.inc("hello")
# print(obj.getMaxKey())
# print(obj.getMinKey())
# obj.inc("leet")
# print(obj.getMaxKey())
# print(obj.getMinKey())
# @lc code=end
