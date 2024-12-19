#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        stack: list[int] = []

        for n in arr:
            if not stack or n > stack[-1]:  # create a new chunk
                stack.append(n)
                continue

            max_n = stack[-1]
            while stack and n < stack[-1]:  # concatenate previous chunk
                stack.pop()
            stack.append(max_n)

        return len(stack)


# @lc code=end
