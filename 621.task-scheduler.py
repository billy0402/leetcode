#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#


# @lc code=start
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq: dict[str, int] = {}
        max_cycles = 0

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
            max_cycles = max(max_cycles, freq[task])

        time = (max_cycles - 1) * (n + 1)
        for f in freq.values():
            if f == max_cycles:
                time += 1

        return max(time, len(tasks))


# @lc code=end
