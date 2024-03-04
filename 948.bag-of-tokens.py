#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#


# @lc code=start
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1
        score = 0

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            # we need to check up if there are at least two tokens
            # so we can face down one and face up one back
            elif score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return score


# @lc code=end
