n = int(input())
members = {}
min_age = 201
max_age = 0
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age in members.keys():
        members[age].append(name)
    else:
        members[age] = [name]
        if age < min_age:
            min_age = age
        if age > max_age:
            max_age = age

for age in range(min_age, max_age + 1):
    if age not in members.keys():
        continue
    for member in members[age]:
        print(age, member)