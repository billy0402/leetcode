#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

mapping = {
    90: "Ninety",
    80: "Eighty",
    70: "Seventy",
    60: "Sixty",
    50: "Fifty",
    40: "Forty",
    30: "Thirty",
    20: "Twenty",
    19: "Nineteen",
    18: "Eighteen",
    17: "Seventeen",
    16: "Sixteen",
    15: "Fifteen",
    14: "Fourteen",
    13: "Thirteen",
    12: "Twelve",
    11: "Eleven",
    10: "Ten",
    9: "Nine",
    8: "Eight",
    7: "Seven",
    6: "Six",
    5: "Five",
    4: "Four",
    3: "Three",
    2: "Two",
    1: "One",
}

scale = ["", "Thousand", "Million", "Billion"]


# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        def under_thousand(value: int):
            words: list[str] = []

            if value > 99:
                hundredth, value = divmod(value, 100)
                words.append(mapping[hundredth])
                words.append("Hundred")

            if value > 20:
                tenth, value = divmod(value, 10)
                words.append(mapping[tenth * 10])

            if value > 0:
                words.append(mapping[value])

            return " ".join(words)

        if num == 0:
            return "Zero"

        result: list[str] = []
        i = 0
        while num:
            num, current = divmod(num, 1000)
            sentence = under_thousand(current)
            if sentence:
                if scale[i]:
                    result.append(scale[i])
                result.append(sentence)
            i += 1
        return " ".join(reversed(result))


# @lc code=end
