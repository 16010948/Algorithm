MOTHS = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
}
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day, year, hour, minute = input().replace(",", "").replace(":", " ").split()
total_time = 365 * 24 * 60

year = int(year)
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    total_time += 24 * 60
    days[2] = 29

sum_time = 0
for m in range(1, MOTHS[month]):
    sum_time += days[m] * 24 * 60
sum_time += (int(day) - 1) * 24 * 60 + int(hour) * 60 + int(minute)

print((sum_time / total_time) * 100)


