#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from enum import StrEnum


class Operator(StrEnum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLIED = '*'
    DIVIDED = '/'


ListOperator = list(Operator)


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def calculate(left: int, right: int, operator: Operator) -> int:
            if operator == Operator.PLUS:
                return left + right
            elif operator == Operator.MINUS:
                return left - right
            elif operator == Operator.MULTIPLIED:
                return left * right
            elif operator == Operator.DIVIDED:
                return int(left / right)

        stack_nums = []
        for token in tokens:
            if token in ListOperator:
                right = stack_nums.pop()
                left = stack_nums.pop()
                result = calculate(left, right, token)
                stack_nums.append(result)
            else:
                stack_nums.append(int(token))
        return stack_nums.pop()


# @lc code=end
