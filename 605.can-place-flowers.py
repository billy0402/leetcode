#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#


# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        planted = 0
        for i in range(len(flowerbed)):
            empty_left = i == 0 or not flowerbed[i - 1]
            empty_center = not flowerbed[i]
            empty_right = i == len(flowerbed) - 1 or not flowerbed[i + 1]

            if empty_left and empty_center and empty_right:
                flowerbed[i] = 1
                planted += 1

                if planted >= n:
                    return True

        return False


# @lc code=end
