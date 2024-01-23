#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        temp = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or temp > 0:
            if i >= 0:
                temp += int(a[i])
                i -= 1

            if j >= 0:
                temp += int(b[j])
                j -= 1

            answer.append(str(temp % 2))
            temp //= 2
        return ''.join(reversed(answer))


# @lc code=end
