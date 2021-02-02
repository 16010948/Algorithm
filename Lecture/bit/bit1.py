def get_bit(n, i):
    return n & (1 << i) != 0

# 1 0 0 1
print(get_bit(9, 3))
# 0 1 0 1
print(get_bit(6, 3))