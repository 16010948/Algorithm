def clear_right_bit(n, i):
    return n & (-1 << (i + 1))

# 1 0 1 0 1 0 0 1
# 1 0 1 0 0 0 0 0
print(clear_right_bit(169, 3))