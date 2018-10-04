# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

print 'sum and mean'
arr = np.random.randn(5, 4)
print arr
print arr.mean()
print arr.sum()
print arr.mean(axis = 1)  #
print arr.sum(0) 
print


print 'cunsum and cumprod function'
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print arr.cumsum(0)
print arr.cumprod(1)
