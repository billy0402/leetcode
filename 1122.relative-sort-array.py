#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counter: dict[int, int] = defaultdict(int)
        nums = set(arr2)

        not_in: list[int] = []
        for num in arr1:
            if num in nums:
                counter[num] += 1
            else:
                not_in.append(num)
        not_in.sort()

        answer: list[int] = []
        for num in arr2:
            for _ in range(counter[num]):
                answer.append(num)

        return answer + not_in


# @lc code=end
