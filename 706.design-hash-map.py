#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
MAX_SIZE = 10**6 + 1


class MyHashMap:
    values: list[int]

    def __init__(self):
        self.values = [-1] * MAX_SIZE

    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        return self.values[key]

    def remove(self, key: int) -> None:
        self.values[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(1, 1)
# obj.put(2, 2)
# r = obj.get(1)
# print(r)
# r = obj.get(3)
# print(r)
# obj.put(2, 1)
# r = obj.get(2)
# print(r)
# obj.remove(2)
# r = obj.get(2)
# print(r)
# @lc code=end
