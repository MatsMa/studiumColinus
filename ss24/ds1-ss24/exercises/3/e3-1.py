import numpy as np

# a)
rows = 8
cols = 5
start_value = 1.0

arr = np.arange(start_value, start_value + 0.5 * rows * cols, 0.5).reshape(
    rows, cols
)
# print(arr)

# b)
int_mask = np.mod(arr, 1) == 0
# print(int_mask)

# c)
# Find indexes
arr_flat = np.ravel(arr)
mask_flat = np.ravel(int_mask)
indexes = []
for idx, el in enumerate(mask_flat):
    if el:
        indexes.append(idx)

print(indexes)
ints = np.take(arr_flat, indexes)

# Split into two
s1, s2 = np.split(ints, 2)
print(s1)
print(s2)

# Row-wise mean
print(np.mean(arr, axis=1))

# Column-wise mean
print(np.mean(arr, axis=0))
