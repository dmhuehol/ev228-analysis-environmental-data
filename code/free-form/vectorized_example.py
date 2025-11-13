'''vectorized_example
Contrast efficiency of loop-based and vectorized approaches for array addition.
'''

import time

import numpy as np

#  Example 2D faux-dataset
arr_ones = np.ones([1000, 720, 1440])
arr_twos = np.ones([1000, 720, 1440]) * 2
shape = np.shape(arr_ones)
print(shape)
arr_sum = np.zeros(shape)
count_indices = len(arr_ones)

#  Loop-based array addition
sum_val = 0
tic = time.time()
for lat in np.arange(0, shape[0]):
    for lon in np.arange(0, shape[1]):
        arr_sum[lat, lon] = arr_ones[lat, lon] + arr_twos[lat, lon]
print(arr_sum)
toc = time.time() - tic
print('Loop time: ' + str(toc))

#  Vectorized array addition
tic = time.time()
arr_sum_vec = arr_ones + arr_twos
toc = time.time() - tic
print('Vectorized time: ' + str(toc))
print(arr_sum_vec)
print(np.array_equal(arr_sum_vec, arr_sum))
