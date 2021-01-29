import sys

def check_mode(frequency):
    max_mode = max(frequency.values())
    modes = [k for k, v in frequency.items() if max_mode == v]
    if len(modes) >= 2:
        modes.sort()
        return modes[1]
    else:
        return modes[0]

n = int(sys.stdin.readline())
array = []
total = 0
frequency = {}
for i in range(n):
    array.append(int(sys.stdin.readline()))
    total += array[i]
    if array[i] in frequency.keys():
        frequency[array[i]] += 1
    else:
        frequency[array[i]] = 1
avg = round(total / n)
array.sort()
mode = check_mode(frequency)

print(avg)
print(array[n // 2])
print(mode)
print(array[n - 1] - array[0])