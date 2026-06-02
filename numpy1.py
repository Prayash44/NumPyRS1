import numpy as np

a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])

# First column
print(a[:,0])

# Last row
print(a[-1])
# [77 88 99]

# Subarray
print(a[:2,1:])