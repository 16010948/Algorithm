def clear_bit(n, i):
    return n & ~(1 << i)

# 1 0 0 1
# 0 0 0 1
print(clear_bit(9, 3))