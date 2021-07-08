print(2, end=" ")
for i in range(3, 1000000, 2):
    is_prime = True
    for j in range(3, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end= " ")
