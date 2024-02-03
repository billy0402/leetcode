#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
MAX_SIZE = 10**6 + 1


class MyHashSet:
    values: list[bool]

    def __init__(self):
        self.values = [False] * MAX_SIZE

    def add(self, key: int) -> None:
        self.values[key] = True

    def remove(self, key: int) -> None:
        self.values[key] = False

    def contains(self, key: int) -> bool:
        return self.values[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# r = obj.contains(1)
# print(r)
# r = obj.contains(3)
# print(r)
# obj.add(2)
# r = obj.contains(2)
# print(r)
# obj.remove(2)
# r = obj.contains(2)
# print(r)
# @lc code=end
