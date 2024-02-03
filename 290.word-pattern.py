#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        texts = s.split(' ')
        if len(pattern) != len(texts):
            return False

        key_values: dict[str, str] = {}
        value_keys: dict[str, str] = {}
        for p, text in zip(pattern, texts):
            if p in key_values and key_values[p] != text:
                return False

            if text in value_keys and value_keys[text] != p:
                return False

            key_values[p] = text
            value_keys[text] = p

        return True


# @lc code=end
