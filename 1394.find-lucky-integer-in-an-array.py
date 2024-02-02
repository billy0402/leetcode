#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#


# @lc code=start
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        answer = -1
        counter: dict[int, int] = {}

        for n in arr:
            counter[n] = counter.get(n, 0) + 1

        for key, value in counter.items():
            if key == value:
                answer = max(answer, key)

        return answer


# @lc code=end
