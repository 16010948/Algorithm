T = int(input())

for test_case in range(1, T + 1):
    directions = input()
    a = 1
    b = 1
    for direction in directions:
        if direction == "L":
            b += a
        else:
            a += b
    print("#"+str(test_case), a, b)
