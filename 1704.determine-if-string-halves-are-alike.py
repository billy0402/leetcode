#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start

vowels = {'a', 'e', 'i', 'o', 'u'}


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        middle = n // 2
        counter = 0

        for i in range(n):
            char = s[i].lower()
            if char in vowels:
                if i < middle:
                    counter += 1
                else:
                    counter -= 1

        return counter == 0


# @lc code=end
