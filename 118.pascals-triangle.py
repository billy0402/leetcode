#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        result = [[1]]

        for _ in range(num_rows - 1):
            temp = [0] + result[-1] + [0]
            row = [temp[j] + temp[j + 1] for j in range(len(result[-1]) + 1)]
            result.append(row)

        return result


# @lc code=end
