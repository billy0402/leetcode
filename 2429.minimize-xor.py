#
# @lc app=leetcode id=2429 lang=python3
#
# [2429] Minimize XOR
#

# @lc code=start
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt1, cnt2 = num1.bit_count(), num2.bit_count()
        x = num1
        i = 0

        while cnt1 != cnt2:
            if cnt1 > cnt2 and x & (1 << i):
                cnt1 -= 1
                x ^= 1 << i

            if cnt1 < cnt2 and x & (1 << i) == 0:
                cnt1 += 1
                x |= 1 << i

            i += 1

        return x


# @lc code=end
