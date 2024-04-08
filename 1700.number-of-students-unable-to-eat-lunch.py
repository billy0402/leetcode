#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#


# @lc code=start
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        circular_counter = 0
        square_counter = 0

        for student in students:
            if student == 0:
                circular_counter += 1
            else:  # 1
                square_counter += 1

        for sandwich in sandwiches:
            if sandwich == 0 and circular_counter:
                circular_counter -= 1
            elif sandwich == 1 and square_counter:
                square_counter -= 1
            else:
                return circular_counter + square_counter

        return 0


# @lc code=end
