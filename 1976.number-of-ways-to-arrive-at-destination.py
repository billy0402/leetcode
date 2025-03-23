#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush

MOD = 10**9 + 7


class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        graph: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((w, v))
            graph[v].append((w, u))

        min_heap: list[tuple[int, int]] = [(0, 0)]  # (cost, node)
        min_cost = [float("inf")] * n
        path_cost = [0] * n
        path_cost[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)

            for nei_cost, nei_node in graph[node]:
                if cost + nei_cost < min_cost[nei_node]:
                    min_cost[nei_node] = cost + nei_cost
                    path_cost[nei_node] = path_cost[node]
                    heappush(min_heap, (cost + nei_cost, nei_node))
                elif cost + nei_cost == min_cost[nei_node]:
                    path_cost[nei_node] = (path_cost[node] + path_cost[nei_node]) % MOD

        return path_cost[n - 1]


# @lc code=end
