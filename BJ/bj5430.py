from _collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    x = input()[1:-1]
    reverse = False
    if len(x) > 0:
        x = deque(list(map(int, x.split(","))))

    try:
        for command in p:
            if command == "R":
                reverse = not reverse
            elif command == "D":
                if reverse:
                    x.pop()
                else:
                    x.popleft()
        result = "["
        if reverse:
            for i in range(len(x) - 1, -1 , -1):
                result += str(x[i]) + ","
        else:
            for i in range(len(x)):
                result += str(x[i]) + ","
        if len(result) > 1:
            result = result[:-1]
        result += "]"
        print(result)
    except:
        print("error")