def cutting_bar(bar, total, count):
    if total == x:
        return count

    if total > x:
        return cutting_bar(bar // 2, total - bar // 2, count)
    else:
        return cutting_bar(bar // 2, total + bar // 2, count + 1)


x = int(input())
print(cutting_bar(64, 64, 1))