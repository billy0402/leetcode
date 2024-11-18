#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        decrypted = [0] * n

        cur_sum = 0
        l = 0
        for r in range(n + abs(k)):
            cur_sum += code[r % n]

            if r - l + 1 > abs(k):
                cur_sum -= code[l % n]
                l = (l + 1) % n

            if r - l + 1 == abs(k):
                if k > 0:
                    decrypted[(l - 1) % n] = cur_sum
                elif k < 0:
                    decrypted[(r + 1) % n] = cur_sum

        return decrypted


# @lc code=end
