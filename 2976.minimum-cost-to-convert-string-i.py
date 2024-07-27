#
# @lc app=leetcode id=2976 lang=python3
#
# [2976] Minimum Cost to Convert String I
#

# @lc code=start
class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: list[str],
        changed: list[str],
        cost: list[int],
    ) -> int:
        def get_index(char: str):
            return ord(char) - ord("a")

        total_cost = 0
        graph = [[float("inf")] * 26 for _ in range(26)]

        for i in range(26):
            graph[i][i] = 0

        for src, dst, cur_cost in zip(original, changed, cost, strict=True):
            x = get_index(src)
            y = get_index(dst)
            graph[x][y] = min(graph[x][y], cur_cost)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        for src, dst in zip(source, target, strict=True):
            x = get_index(src)
            y = get_index(dst)
            cur_cost = graph[x][y]
            if cur_cost == float("inf"):
                return -1
            total_cost += cur_cost

        return total_cost


# @lc code=end
