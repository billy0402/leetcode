#
# @lc app=leetcode id=1823 lang=python3
#
# [1823] Find the Winner of the Circular Game
#

# @lc code=start
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i + 1 for i in range(n)]
        i = 0

        while len(friends) > 1:
            i += k - 1
            i %= len(friends)
            friends.pop(i)

        return friends.pop()


# @lc code=end
