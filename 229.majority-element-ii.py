#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        answer = []
        min_appear = len(nums) // 3
        hash_table = {}

        for n in nums:
            hash_table[n] = hash_table.get(n, 0) + 1

            if n not in answer and hash_table[n] > min_appear:
                answer.append(n)

        return answer


# @lc code=end
