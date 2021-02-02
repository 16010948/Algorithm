def set_bit(n, i):
    return n | (1 << i)

# 0 1 0 1
# 1 1 0 1
print(set_bit(5, 3))