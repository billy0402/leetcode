#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t: dict[str, str] = {}
        t_to_s: dict[str, str] = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if char_t != s_to_t[char_s]:
                    return False
            elif char_t in t_to_s:
                if char_s != t_to_s[char_t]:
                    return False
            else:
                s_to_t[char_s] = char_t
                t_to_s[char_t] = char_s

        return True


# @lc code=end
