import re

DAYS_31 = (1, 3, 5, 7, 8, 10, 12)
DAYS_30 = (4, 6, 9, 11)
DAYS_28 = 2

T = int(input())

for test_case in range(1, T + 1):
    date = re.search('(\d{4})(\d{2})(\d{2})', input()).groups()
    year, month, day = map(int, date)
    result = -1
    if (month in DAYS_31 and (day >= 1 and day <= 31)) or \
            (month in DAYS_30 and (day >= 1 and day <= 30)) or \
            (month == DAYS_28 and (day >= 1 and day <= 28)):
        result = '/'.join(date)
    print("#" + str(test_case), result)
