# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as np_random

x_arr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
y_arr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = [(x if c else y) for x, y, c in zip(x_arr, y_arr, cond)] 
print result
print np.where(cond, x_arr, y_arr)  
print

print 'example of using where function'
arr = np_random.randn(4, 4)
print arr
print np.where(arr > 0, 2, -2)
print np.where(arr > 0, 2, arr)
print

print 'where embedding'
cond_1 = np.array([True, False, True, True, False])
cond_2 = np.array([False, True, False, True, False])
# without using the where function
result = []
for i in xrange(len(cond)):
    if cond_1[i] and cond_2[i]:
        result.append(0)
    elif cond_1[i]:
        result.append(1)
    elif cond_2[i]:
        result.append(2)
    else:
        result.append(3)
print result
# using where function
result = np.where(cond_1 & cond_2, 0, \
          np.where(cond_1, 1, np.where(cond_2, 2, 3)))
print result
