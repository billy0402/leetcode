#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque


class Queue(deque):
    def pop(self) -> None:
        self.popleft()


class RecentCounter:
    queue: Queue

    def __init__(self):
        self.queue = Queue()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue and self.queue[0] < t - 3000:
            self.queue.pop()

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# r = obj.ping(1)
# print(r)
# r = obj.ping(100)
# print(r)
# r = obj.ping(3001)
# print(r)
# r = obj.ping(3002)
# print(r)
# @lc code=end
