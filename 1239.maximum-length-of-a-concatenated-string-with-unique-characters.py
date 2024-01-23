#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#


# @lc code=start
class Solution:
    def maxLength(self, arr: list[str]) -> int:
        def backtracking(start_index: int, current: str):
            nonlocal max_length
            max_length = max(max_length, len(current))

            for i in range(start_index, len(arr)):
                s = arr[i]
                if not is_valid(s, current):
                    continue
                backtracking(i + 1, current + s)

        def is_valid(s: str, current: str):
            visited = set(current)
            for char in s:
                if char in visited:
                    return False
                visited.add(char)
            return True

        max_length = 0
        backtracking(0, '')
        return max_length


# @lc code=end
