# -*- coding: utf-8 -*-

import numpy as np

data = [6, 7.5, 8, 0, 1]
arr = np.array(data)
print arr

print arr.dtype
print 


data = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr = np.array(data)
print arr

print arr.shape
print


print np.zeros(10) 
print np.zeros((3, 6)) 
print np.empty((2, 3, 2)) 
print


print np.arange(15)  # [0, 1, 2, ..., 14]
