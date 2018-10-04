# -*- coding: utf-8 -*-

import numpy as np

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
print arr
print arr[[4, 3, 0, 6]] # print arr[4]、arr[3]、arr[0],arr[6]。
print arr[[-3, -5, -7]] # print arr[3]、arr[5],arr[-7]
arr = np.arange(32).reshape((8, 4))  
print arr[[1, 5, 7, 2], [0, 3, 1, 2]] # print arr[1, 0]、arr[5, 3]，arr[7, 1],arr[2, 2]
print arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]  # 1572line 的0312colums
print arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])] 
