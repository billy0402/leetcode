#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#

# @lc code=start
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()

        chemistry_sum = 0
        team_skill = skill[0] + skill[-1]

        for i in range(len(skill) // 2):
            left, right = skill[i], skill[-i - 1]
            if left + right != team_skill:
                return -1

            chemistry_sum += left * right

        return chemistry_sum


# @lc code=end
