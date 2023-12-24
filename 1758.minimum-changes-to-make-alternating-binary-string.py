#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#


# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        zero_counter = 0
        one_counter = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    zero_counter += 1
                else:
                    one_counter += 1
            else:
                if s[i] != '1':
                    zero_counter += 1
                else:
                    one_counter += 1
        return min(zero_counter, one_counter)


# @lc code=end
