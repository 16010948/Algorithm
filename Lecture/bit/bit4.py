def clear_left_bit(n, i):
    return n & ((1 << i) - 1)

# 1 0 1 0 1 0 0 1
print(clear_left_bit(169, 3))