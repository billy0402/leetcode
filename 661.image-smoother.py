#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        results = []
        cols = len(img)
        rows = len(img[0])

        for n in range(cols):
            for m in range(rows):
                count = 0
                total = 0
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if not (0 <= m+x < rows) or \
                           not (0 <= n+y < cols):
                            continue
                        total += img[n + y][m + x]
                        count += 1
                total //= count

                if len(results) <= n:
                    results.append([])
                results[n].append(total)

        return results


# @lc code=end
