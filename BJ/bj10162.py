microwave = (60 * 5, 60 * 1, 10)

t = int(input())
answers = []
for time in microwave:
    answers.append(t // time)
    t %= time

if t != 0:
    print(-1)
else:
    for answer in answers:
        print(answer, end=" ")
