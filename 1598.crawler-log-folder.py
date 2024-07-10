#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0

        for log in logs:
            if log == "../":
                depth = max(depth - 1, 0)
            elif log != "./":
                depth += 1

        return depth


# @lc code=end
