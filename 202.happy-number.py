#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        product = 0
        results = set()

        while True:
            for s in str(n):
                product += (int(s)**2)

            if product == 1:
                return True

            if product in results:
                break
            results.add(product)

            n = product
            product = 0

        return False


# @lc code=end
