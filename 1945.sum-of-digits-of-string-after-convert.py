#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = 0

        for char in s:
            ascii_code = ord(char) - ord("a") + 1
            while ascii_code > 0:
                total += ascii_code % 10
                ascii_code //= 10

        for _ in range(1, k):
            current = 0
            while total > 0:
                current += total % 10
                total //= 10
            total = current

        return total


# @lc code=end
