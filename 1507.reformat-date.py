#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#

# @lc code=start
MONTHS = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}


class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')
        return f'{year}-{MONTHS[month]}-{day[:-2].zfill(2)}'


# @lc code=end
