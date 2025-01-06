#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n

        for j in range(n):
            if boxes[j] != "1":
                continue

            for i in range(n):
                answer[i] += abs(i - j)

        return answer


# @lc code=end
