def update_bit(n, i, val):
    return (n & ~(1 << i)) | ((1 if val else 0) << i)

# 1 0 1 0 1 0 0 1
# 1 0 1 0 0 0 0 1
print(update_bit(169, 3, False))