#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_table: dict[str, str] = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s in hash_table:
                hash_table[sorted_s].append(s)
            else:
                hash_table[sorted_s] = [s]

        answer = list(hash_table.values())
        return answer


# @lc code=end
