#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:
    values: list
    indexes: dict

    def __init__(self):
        self.values = list()
        self.indexes = dict()

    def is_exists(self, val: int) -> bool:
        return val in self.indexes

    def insert(self, val: int) -> bool:
        if self.is_exists(val):
            return False

        self.values.append(val)
        self.indexes[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.is_exists(val):
            return False

        i = self.indexes[val]
        last = self.values[-1]
        self.values[i] = last
        self.indexes[last] = i

        self.values.pop()
        del self.indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# r = obj.insert(1)
# print(r)
# r = obj.remove(2)
# print(r)
# r = obj.insert(2)
# print(r)
# r = obj.getRandom()
# print(r)
# r = obj.remove(1)
# print(r)
# r = obj.insert(2)
# print(r)
# r = obj.getRandom()
# print(r)

# @lc code=end
