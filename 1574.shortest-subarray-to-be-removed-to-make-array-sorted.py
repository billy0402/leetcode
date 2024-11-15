#
# @lc app=leetcode id=1574 lang=python3
#
# [1574] Shortest Subarray to be Removed to Make Array Sorted
#

# @lc code=start
class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        sub_length = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            sub_length = min(sub_length, right - left - 1)
            left += 1
        return sub_length


# @lc code=end
