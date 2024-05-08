#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#


# @lc code=start
class Solution:
    def findRelativeRanks(self, scores: list[int]) -> list[str]:
        sorted_scores = sorted(scores, reverse=True)
        # { score: index }
        sorted_scores_map: dict[int, int] = {}
        for index, score in enumerate(sorted_scores):
            sorted_scores_map[score] = index

        answer: list[str] = []
        for score in scores:
            rank = sorted_scores_map[score] + 1

            if rank == 1:
                answer.append('Gold Medal')
            elif rank == 2:
                answer.append('Silver Medal')
            elif rank == 3:
                answer.append('Bronze Medal')
            else:
                answer.append(str(rank))

        return answer


# @lc code=end
