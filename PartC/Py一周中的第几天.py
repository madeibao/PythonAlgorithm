from datetime import datetime

def getWeekDay(day, month, year):
    d = datetime(year, month, day)
    week_map = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return week_map[d.weekday()]

class Solution:
    pass

if __name__ == '__main__':
    print(getWeekDay(17, 9, 2026))  # Thursday
