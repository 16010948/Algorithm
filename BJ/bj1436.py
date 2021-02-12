n = int(input())

count = 0
title = 665
while count < n:
    title += 1
    if '666' in str(title):
        count += 1
print(title)