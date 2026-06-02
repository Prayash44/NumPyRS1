import numpy as np
a = np.arange(1,13)


print(a.reshape(3,4))
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(a.reshape(2,6))
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]]

print(a.reshape(2,3,2))
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]