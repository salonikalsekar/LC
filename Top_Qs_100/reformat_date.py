class Solution:
    def reformatDate(self, date: str) -> str:
        dates = date.split()
        res = ""
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

        for i in range(len(dates) - 1, -1, -1):
            if i == 0:
                if len(dates[i][:-2]) < 2:
                    res += "0" + dates[i][:-2]
                else:
                    res += dates[i][:-2]
            elif i == 1:
                res += months[dates[i]] + "-"
            elif i == 2:
                res += dates[i] + '-'

        return res