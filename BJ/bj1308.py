def calc_day(s_year, year, month, day):
    d_day = day
    for y in range(s_year, year):
        d_day += 365
        if is_leap_year(y):
            d_day += 1

    for m in range(1, month):
        d_day += DAYS[m]
        if m == 2 and is_leap_year(year):
            d_day += 1
    return d_day

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


start_year, start_month, start_day = map(int, input().split())
end_year, end_month, end_day = map(int, input().split())

if start_year + 1000 <= end_year and start_month <= end_month and start_day <= end_day:
    print("gg")
else:
    start = calc_day(start_year, start_year, start_month, start_day)
    end = calc_day(start_year, end_year, end_month, end_day)
    d_day = end - start
    print("D-" + str(d_day))