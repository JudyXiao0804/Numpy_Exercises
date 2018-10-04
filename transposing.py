# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

arr = np.arange(15).reshape((3, 5))
print arr
print arr.T
print

arr = np_random.randn(6, 3)
print np.dot(arr.T, arr)
print

arr = np.arange(16).reshape((2, 2, 4))
print arr

'''
- a[0][0] = [0, 1, 2, 3]
- a[0][1] = [4, 5, 6, 7]
- a[1][0] = [8, 9, 10, 11]
- a[1][1] = [12, 13, 14, 15]

- a'[0][0] = a[0][0] = [0, 1, 2, 3]
- a'[0][1] = a[1][0] = [8, 9, 10, 11]
- a'[1][0] = a[0][1] = [4, 5, 6, 7]
- a'[1][1] = a[1][1] = [12, 13, 14, 15]
'''
print arr.transpose((1, 0, 2))
print arr.swapaxes(1, 2)  
